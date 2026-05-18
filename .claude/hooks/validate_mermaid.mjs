#!/usr/bin/env node
import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const HOOKS_DIR = dirname(fileURLToPath(import.meta.url));
const CACHE_PATH = resolve(HOOKS_DIR, '.mermaid-cache.json');
const BLOCK_RE = /```mermaid\b[^\n]*\n([\s\S]*?)\n?```/g;

const mode = process.argv.find(a => a.startsWith('--mode='))?.split('=')[1];
if (mode !== 'file' && mode !== 'stop') process.exit(0);

const event = JSON.parse(await readStdin());

let blocks;
let sourceLabel;
if (mode === 'file') {
  const fp = event.tool_input?.file_path;
  if (!fp || !fp.endsWith('.md') || !existsSync(fp)) process.exit(0);
  blocks = extractBlocks(readFileSync(fp, 'utf8'));
  sourceLabel = fp;
} else {
  const tp = event.transcript_path;
  if (!tp || !existsSync(tp)) process.exit(0);
  const text = lastAssistantText(tp);
  if (!text) process.exit(0);
  blocks = extractBlocks(text);
  sourceLabel = 'chat response';
}

if (blocks.length === 0) process.exit(0);

const cache = readCache();
const toValidate = [];
for (const content of blocks) {
  const hash = sha256(content);
  if (cache[hash] === 'ok') continue;
  toValidate.push({ content, hash });
}
if (toValidate.length === 0) process.exit(0);

let mermaid;
try {
  const { JSDOM } = await import('jsdom');
  const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');
  globalThis.window = dom.window;
  globalThis.document = dom.window.document;
  globalThis.HTMLElement = dom.window.HTMLElement;
  globalThis.Node = dom.window.Node;
  globalThis.DocumentFragment = dom.window.DocumentFragment;
  mermaid = (await import('mermaid')).default;
  mermaid.initialize({ startOnLoad: false, securityLevel: 'loose' });
} catch (e) {
  process.stderr.write(`[validate-mermaid] cannot load mermaid/jsdom (${e.message}). Run: cd .claude/hooks && npm install\n`);
  process.exit(0);
}

const results = await Promise.all(toValidate.map(async (b, i) => {
  try {
    await mermaid.parse(b.content);
    return { ok: true, i, hash: b.hash };
  } catch (e) {
    return { ok: false, i, error: (e?.message || String(e)).trim() };
  }
}));

for (const r of results) if (r.ok) cache[r.hash] = 'ok';
writeCache(cache);

const errors = results.filter(r => !r.ok);
if (errors.length > 0) {
  const reason = formatReason(sourceLabel, errors, toValidate);
  process.stdout.write(JSON.stringify({ decision: 'block', reason }));
}
process.exit(0);

function extractBlocks(text) {
  const out = [];
  let m;
  BLOCK_RE.lastIndex = 0;
  while ((m = BLOCK_RE.exec(text)) !== null) {
    const body = m[1].replace(/\s+$/, '');
    if (body.length > 0) out.push(body);
  }
  return out;
}

function lastAssistantText(transcriptPath) {
  const lines = readFileSync(transcriptPath, 'utf8').split('\n');
  for (let i = lines.length - 1; i >= 0; i--) {
    const line = lines[i].trim();
    if (!line) continue;
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }
    if (entry.type !== 'assistant') continue;
    const content = entry.message?.content;
    if (!Array.isArray(content)) continue;
    const texts = content.filter(c => c.type === 'text' && typeof c.text === 'string').map(c => c.text);
    if (texts.length > 0) return texts.join('\n');
  }
  return '';
}

function readCache() {
  if (!existsSync(CACHE_PATH)) return {};
  try { return JSON.parse(readFileSync(CACHE_PATH, 'utf8')); } catch { return {}; }
}

function writeCache(cache) {
  try { writeFileSync(CACHE_PATH, JSON.stringify(cache, null, 2)); } catch {}
}

function sha256(s) {
  return createHash('sha256').update(s).digest('hex');
}

function formatReason(label, errors, blocks) {
  const lines = [`Mermaid validation failed in ${label}:`];
  for (const e of errors) {
    const preview = blocks[e.i].content.split('\n').slice(0, 2).join(' / ').slice(0, 80);
    lines.push(`Block #${e.i + 1} ("${preview}"): ${e.error}`);
  }
  lines.push('', 'Fix the mermaid syntax and re-emit the block.');
  return lines.join('\n');
}

function readStdin() {
  return new Promise((res, rej) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', c => data += c);
    process.stdin.on('end', () => res(data));
    process.stdin.on('error', rej);
  });
}

"use strict";

const $ = (sel, root = document) => root.querySelector(sel);
const el = (tag, cls, html) => {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (html != null) n.innerHTML = html;
  return n;
};
const esc = (s) =>
  (s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

const METRICS = [
  ["factual_correctness", "Factual"],
  ["focus", "Focus"],
  ["clarity", "Clarity"],
];

let stream = null; // current EventSource

// --------------------------------------------------------------- views
function showView(name) {
  $("#view-upload").classList.toggle("active", name === "upload");
  $("#view-results").classList.toggle("active", name === "results");
}

function showUploadMsg(text) {
  const m = $("#upload-msg");
  m.textContent = text;
  m.hidden = false;
}

// --------------------------------------------------------------- demo / upload
async function useDemo() {
  $("#upload-msg").hidden = true;
  try {
    const list = await (await fetch("/api/interviews")).json();
    if (Array.isArray(list) && list.length) {
      run(list[0].source_id);
    } else {
      showUploadMsg("Демо-данные не найдены.");
    }
  } catch {
    showUploadMsg("Не удалось загрузить демо.");
  }
}

async function onFile(file) {
  if (!file) return;
  $("#upload-msg").hidden = true;
  const text = await file.text();
  let res = {};
  try {
    res = await (await fetch("/api/match", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    })).json();
  } catch { /* fall through to message */ }

  if (res.source_id) {
    run(res.source_id);
  } else {
    showUploadMsg("Не удалось обработать этот файл. Попробуйте «Use demo».");
  }
}

// --------------------------------------------------------------- run one transcript
function run(sourceId) {
  if (stream) { stream.close(); stream = null; }

  $("#qa").innerHTML = "";
  $("#verdict").hidden = true;
  $("#run-title").textContent =
    sourceId.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

  const status = $("#status");
  status.hidden = false;

  showView("results");
  startStream(sourceId);
}

function backToUpload() {
  if (stream) { stream.close(); stream = null; }
  $("#qa").innerHTML = "";
  $("#verdict").hidden = true;
  $("#status").hidden = true;
  $("#upload-msg").hidden = true;
  showView("upload");
  if (location.search) history.replaceState(null, "", location.pathname);
}

function startStream(sourceId) {
  stream = new EventSource(`/api/stream?source_id=${encodeURIComponent(sourceId)}`);

  let total = 0;

  stream.addEventListener("split_item", (e) => {
    const it = JSON.parse(e.data);
    total = Math.max(total, it.idx + 1);
    addCard(it);
  });

  stream.addEventListener("score_item", (e) => fillScore(JSON.parse(e.data)));

  stream.addEventListener("report", (e) => renderVerdict(JSON.parse(e.data)));

  stream.addEventListener("done", () => {
    $("#status").hidden = true;
    stream.close();
    stream = null;
  });

  stream.onerror = () => {
    $("#status").hidden = true;
    if (stream) { stream.close(); stream = null; }
  };
}

// --------------------------------------------------------------- rendering
function addCard(it) {
  const li = el("li", "qa-card");
  li.id = `card-${it.idx}`;
  const meta = [it.question_type, it.question_topic, it.interview_stage]
    .filter(Boolean)
    .map((m) => `<span class="pill">${esc(m)}</span>`)
    .join("");
  li.innerHTML = `
    <div class="qhead">
      <span class="qnum">${esc(it.id || "Q" + (it.idx + 1))}</span>
      <span class="time pill">${esc(it.question_time || "")}</span>
    </div>
    <div class="q">${esc(it.question || "(нет текста вопроса)")}</div>
    <div class="a">${esc(it.answer || "(нет ответа)")}</div>
    <div class="meta">${meta}</div>
    <div class="pending"><span class="dot"></span> оцениваю…</div>`;
  $("#qa").appendChild(li);
}

function fillScore(s) {
  const card = $(`#card-${s.idx}`);
  if (!card) return;
  const pending = $(".pending", card);
  if (pending) pending.remove();

  if (!s.scored) {
    card.appendChild(el("div", "no-signal",
      "Нет сигнала интервьюера — оценка не выставлена" +
      (s.unscored_reason ? ` (${esc(s.unscored_reason)})` : "")));
    return;
  }

  const boxes = METRICS.map(([key, label]) => {
    const v = s[key];
    const pct = v == null ? 0 : (v / 10) * 100;
    return `
      <div class="score-box">
        <div class="label">${label}</div>
        <div class="val">${v ?? "—"}<small style="font-size:13px;color:var(--muted)">/10</small></div>
        <div class="bar"><i style="width:${pct}%"></i></div>
      </div>`;
  }).join("");

  const wrap = el("div");
  wrap.innerHTML = `<div class="scores">${boxes}</div>`;
  if (s.aggregate) {
    wrap.innerHTML += `<div class="agg">Итог: <span class="chip ${esc(s.aggregate)}">${esc(s.aggregate)}</span></div>`;
  }
  if (s.rationale) {
    wrap.innerHTML += `<div class="rationale">${esc(s.rationale)}</div>`;
  }
  card.appendChild(wrap);
}

function renderVerdict(r) {
  const v = $("#verdict");
  v.hidden = false;
  if (r.verdict == null) {
    v.className = "verdict";
    v.innerHTML = `<div class="metric">Недостаточно оценённых ответов для вывода.</div>`;
    return;
  }
  v.className = "verdict " + (r.verdict === "HIRE" ? "hire" : "nohire");
  const means = METRICS.map(([k, label]) =>
    `<div class="metric">${label}: <b>${r.means[k] ?? "—"}</b></div>`).join("");
  v.innerHTML = `
    <div class="badge">${esc(r.verdict)}</div>
    <div class="metric">p(hire) <b>${r.p_hire ?? "—"}%</b></div>
    <div class="metric">overall <b>${r.overall ?? "—"}/10</b></div>
    ${means}
    <div class="metric">${r.n_scored}/${r.n_questions} оценено</div>`;
}

// --------------------------------------------------------------- wiring
$("#use-demo").addEventListener("click", useDemo);
$("#back").addEventListener("click", backToUpload);
$("#file").addEventListener("change", (e) => {
  onFile(e.target.files[0]);
  e.target.value = "";
});

// drag & drop on the dropzone
const drop = $("#drop");
["dragenter", "dragover"].forEach((ev) =>
  drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.add("over"); }));
["dragleave", "drop"].forEach((ev) =>
  drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.remove("over"); }));
drop.addEventListener("drop", (e) => onFile(e.dataTransfer.files[0]));

// deep link ?sid=… → straight to results
const sid = new URLSearchParams(location.search).get("sid");
if (sid) run(sid);

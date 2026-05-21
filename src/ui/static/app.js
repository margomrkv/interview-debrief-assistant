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

// --------------------------------------------------------------- sidebar
async function loadInterviews() {
  const list = await (await fetch("/api/interviews")).json();
  const ul = $("#interviews");
  ul.innerHTML = "";
  for (const iv of list) {
    const li = el("li");
    li.dataset.sid = iv.source_id;
    const topics = (iv.topics || []).slice(0, 3).map((t) => `<span class="pill">${esc(t)}</span>`).join("");
    li.innerHTML = `
      <div class="it-title">${esc(iv.title)}</div>
      <div class="it-sub">
        <span class="pill">${esc(iv.grade || "—")}</span>
        <span>${iv.n_scored}/${iv.n_questions} оценено</span>
      </div>
      <div class="it-sub">${topics}</div>`;
    li.addEventListener("click", () => run(iv.source_id));
    ul.appendChild(li);
  }
}

// --------------------------------------------------------------- run one transcript
async function run(sourceId) {
  if (stream) { stream.close(); stream = null; }

  document.querySelectorAll("#interviews li").forEach((li) =>
    li.classList.toggle("active", li.dataset.sid === sourceId));

  $("#empty").hidden = true;
  $("#run").hidden = false;
  $("#qa").innerHTML = "";
  $("#verdict").hidden = true;
  $("#progress").textContent = "";
  setStep("splitter", "");
  setStep("scoring", "");

  // transcript preview
  const t = await (await fetch(`/api/transcript?source_id=${encodeURIComponent(sourceId)}`)).json();
  $("#run-title").textContent = sourceId.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  $("#transcript-text").textContent = t.text || "(нет транскрипта)";

  startStream(sourceId);
}

function setStep(name, state) {
  const node = $(`#step-${name}`);
  node.classList.remove("active", "done");
  if (state) node.classList.add(state);
}

function startStream(sourceId) {
  stream = new EventSource(`/api/stream?source_id=${encodeURIComponent(sourceId)}`);

  stream.addEventListener("stage", (e) => {
    const d = JSON.parse(e.data);
    if (d.status === "running") {
      setStep(d.stage, "active");
      $("#progress").textContent =
        d.stage === "splitter"
          ? `Splitter: извлекаю вопросы… (0/${d.total})`
          : `Scoring: оцениваю ответы… (0/${d.total})`;
    } else if (d.status === "done") {
      setStep(d.stage, "done");
    }
  });

  let nSplit = 0, nScore = 0, total = 0;

  stream.addEventListener("split_item", (e) => {
    const it = JSON.parse(e.data);
    total = Math.max(total, it.idx + 1);
    addCard(it);
    nSplit++;
    $("#progress").textContent = `Splitter: извлекаю вопросы… (${nSplit})`;
  });

  stream.addEventListener("score_item", (e) => {
    const s = JSON.parse(e.data);
    fillScore(s);
    nScore++;
    $("#progress").textContent = `Scoring: оцениваю ответы… (${nScore}/${total})`;
  });

  stream.addEventListener("report", (e) => renderVerdict(JSON.parse(e.data)));

  stream.addEventListener("done", () => {
    $("#progress").textContent = "Готово.";
    stream.close();
    stream = null;
  });

  stream.onerror = () => {
    $("#progress").textContent = "Поток прерван.";
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
      <span class="qnum">${it.id || "Q" + (it.idx + 1)}</span>
      <span class="time pill">${esc(it.question_time || "")}</span>
    </div>
    <div class="q">${esc(it.question || "(нет текста вопроса)")}</div>
    <div class="a">${esc(it.answer || "(нет ответа)")}</div>
    <div class="meta">${meta}</div>
    <div class="pending"><span class="dot"></span> ожидает оценки…</div>`;
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
    <div class="badge">${r.verdict}</div>
    <div class="metric">p(hire) <b>${r.p_hire ?? "—"}%</b></div>
    <div class="metric">overall <b>${r.overall ?? "—"}/10</b></div>
    ${means}
    <div class="metric">${r.n_scored}/${r.n_questions} оценено</div>`;
}

// --------------------------------------------------------------- upload
$("#file").addEventListener("change", async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const text = await file.text();
  const res = await (await fetch("/api/match", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  })).json();
  if (res.source_id) {
    run(res.source_id);
  } else {
    $("#empty").hidden = false;
    $("#run").hidden = true;
    $("#empty").textContent = "Загруженный транскрипт не сопоставлен ни с одним известным интервью.";
  }
  e.target.value = "";
});

loadInterviews().then(() => {
  const sid = new URLSearchParams(location.search).get("sid");
  if (sid) run(sid);
});

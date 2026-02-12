const form = document.getElementById("curriculumForm");
const statusBox = document.getElementById("status");
const resultBox = document.getElementById("result");

if (form) {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    statusBox.innerText = "Generating curriculum... ⏳";
    resultBox.innerHTML = "";

    const payload = {
      skill: document.getElementById("skill").value,
      level: document.getElementById("level").value,
      semesters: parseInt(document.getElementById("semesters").value),
      weekly_hours: document.getElementById("weekly_hours").value,
      industry_focus: document.getElementById("industry_focus").value
    };

    try {
      const res = await fetch("/api/generate-curriculum", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();

      if (!res.ok) throw new Error(data.error || "Server error");

      statusBox.innerText = "Curriculum generated ✅";
      renderCurriculum(data);

    } catch (err) {
      statusBox.innerText = "Failed ❌";
      resultBox.innerHTML = `
        <div class="glass-card">
          <pre>${escapeHtml(err.message)}</pre>
        </div>
      `;
    }
  });
}

function renderCurriculum(data) {
  resultBox.innerHTML = `
    <div class="glass-card">
      <h2 class="result-title">${escapeHtml(data.program_title)}</h2>
      <p class="result-summary">${escapeHtml(data.summary)}</p>
    </div>
  `;

  data.semesters.forEach((sem) => {
    const semDiv = document.createElement("div");
    semDiv.className = "semester";

    semDiv.innerHTML = `<h3>Semester ${sem.semester}</h3>`;

    sem.courses.forEach((course) => {
      const courseDiv = document.createElement("div");
      courseDiv.className = "course";

      const topicsHtml = course.topics
        .map((t) => `<span class="topic">${escapeHtml(t)}</span>`)
        .join("");

      courseDiv.innerHTML = `
        <h4>${escapeHtml(course.course_name)}</h4>
        <div class="course-meta">Credits: ${course.credits}</div>
        <div class="topics">${topicsHtml}</div>
      `;

      semDiv.appendChild(courseDiv);
    });

    resultBox.appendChild(semDiv);
  });
}

function escapeHtml(text) {
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
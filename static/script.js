const form = document.getElementById("curriculumForm");
const statusBox = document.getElementById("status");
const resultBox = document.getElementById("result");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  statusBox.innerText = "Generating curriculum... please wait ⏳";
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

    if (!res.ok) {
      throw new Error("Server error: " + res.status);
    }

    const data = await res.json();

    statusBox.innerText = "Curriculum generated ✅";

    // If backend returns JSON curriculum
    if (data.semesters) {
      renderCurriculum(data);
    }
    // If backend returns raw text
    else if (data.raw_output) {
      resultBox.innerHTML = `<pre>${data.raw_output}</pre>`;
    }
    else {
      resultBox.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    }

  } catch (err) {
    statusBox.innerText = "Failed ❌";
    resultBox.innerHTML = `<pre>${err.message}</pre>`;
  }
});

function renderCurriculum(data) {
  resultBox.innerHTML = "";

  data.semesters.forEach((sem) => {
    const semDiv = document.createElement("div");
    semDiv.className = "semester";

    semDiv.innerHTML = `<h3>Semester ${sem.semester}</h3>`;

    sem.courses.forEach((course) => {
      const courseDiv = document.createElement("div");
      courseDiv.className = "course";

      courseDiv.innerHTML = `
        <h4>${course.course_name} (${course.credits} credits)</h4>
        <div class="topics">
          <b>Topics:</b> ${course.topics.join(", ")}
        </div>
      `;

      semDiv.appendChild(courseDiv);
    });

    resultBox.appendChild(semDiv);
  });
}

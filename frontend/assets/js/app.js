const API_URL = "http://127.0.0.1:8000/generate";

async function generatePrep() {
  const role = document.getElementById("role").value.trim();
  const resume = document.getElementById("resume").value.trim();
  const resultBox = document.getElementById("result");

  if (!role || !resume) {
    resultBox.textContent = "Please enter both target role and resume/skills.";
    return;
  }

  resultBox.textContent = "Generating your personalized interview preparation report...";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        resume_text: resume,
        target_role: role
      })
    });

    const data = await response.json();

    if (!response.ok) {
      resultBox.textContent = "Something went wrong. Please check your input or backend.";
      return;
    }

    resultBox.textContent = data.result + (data.note ? "\n\nNote: " + data.note : "");
  } catch (error) {
    resultBox.textContent = "Backend is not running. Start it using: cd backend && uvicorn main:app --reload";
  }
}

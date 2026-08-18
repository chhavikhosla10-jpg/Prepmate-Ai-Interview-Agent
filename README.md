# PrepMate AI – IBM Cloud Powered Interview Preparation Agent

PrepMate AI is an AI-powered interview preparation web application designed for students and freshers. It generates personalized interview preparation based on the candidate's skills, resume information, target role, and job description.

## Live Demo

**Frontend:**
https://prepmate-ai-interview-agent.netlify.app/

**Backend API:**
https://prepmate-ai-interview-agent.onrender.com/

## Problem Statement

Students often prepare for internships and placements using generic interview questions. They need personalized preparation based on their skills, projects, resume information, and the requirements of the target position.

## Solution

PrepMate AI allows users to provide three inputs:

* **Target Role** – The position the candidate is preparing for.
* **Job Description** – The responsibilities and required skills for the position.
* **Resume / Skills / Projects** – The candidate's background, skills, projects, and experience.

The application uses these inputs to generate a personalized interview preparation report.

## Features

* Target role input
* Job description input
* Resume / skills / projects input
* Personalized candidate summary
* HR interview questions
* Technical interview questions
* Strong model answers
* 7-day learning roadmap
* Final confidence tips
* AI-powered interview preparation
* Responsive frontend
* FastAPI backend
* IBM Granite integration
* Fallback mode when IBM credentials are unavailable

## IBM Cloud Services Used

* IBM watsonx.ai
* IBM Granite Foundation Model

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, FastAPI
* **AI:** IBM watsonx.ai / IBM Granite
* **Version Control:** Git, GitHub
* **Deployment:** Netlify, Render

## Folder Structure

```text
PrepMate-Ai-Interview-Agent/
├── backend/
│   ├── main.py
│   ├── routes/
│   │   ├── health.py
│   │   └── interview.py
│   ├── services/
│   │   ├── ibm_granite.py
│   │   └── prompt_builder.py
│   ├── models/
│   │   └── schemas.py
│   ├── utils/
│   │   ├── config.py
│   │   └── helpers.py
│   └── .env.example
├── frontend/
│   ├── index.html
│   ├── dashboard.html
│   ├── results.html
│   └── assets/
├── screenshots/
│   ├── dashboard.png
│   └── report.png
├── tests/
├── deployment/
├── requirements.txt
├── render.yaml
└── README.md
```

## Run Backend Locally

```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

## Run Frontend Locally

Open:

```text
frontend/index.html
```

You can also use VS Code Live Server.

## API Endpoint

```text
POST /generate
```

Example request:

```json
{
  "resume_text": "HTML, CSS, JavaScript, React.js, Git, REST APIs",
  "target_role": "Frontend Developer Intern",
  "job_description": "We are looking for a Frontend Developer Intern with knowledge of HTML, CSS, JavaScript, React.js, REST APIs, Git, responsive design, and debugging."
}
```

## Environment Variables

Create `backend/.env` using `backend/.env.example`.

```text
IBM_API_KEY=your_key_here
IBM_PROJECT_ID=your_project_id_here
IBM_REGION=your_region_here
```

Never commit your actual IBM API key to GitHub.

## Generated Interview Report

The application generates:

1. Personalized Candidate Summary
2. HR Interview Questions
3. Technical Interview Questions
4. Strong Model Answers
5. 7-Day Learning Roadmap
6. Final Confidence Tips

## Screenshots

### Opening Page
![PrepMate AI Opening Page](screenshots/home.png)

### Dashboard
![PrepMate AI Dashboard](screenshots/dashboard.png)

### Generated Output – Part 1
![PrepMate AI Generated Output Part 1](screenshots/output-1.png)

### Generated Output – Part 2
![PrepMate AI Generated Output Part 2](screenshots/output-2.png)

## Deployment

The frontend is deployed using Netlify and the FastAPI backend is deployed using Render.

**Frontend:** https://prepmate-ai-interview-agent.netlify.app/

**Backend:** https://prepmate-ai-interview-agent.onrender.com/

## Author

**Chhavi Khosla**

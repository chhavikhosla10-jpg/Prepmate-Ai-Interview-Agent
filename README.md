# PrepMate AI – IBM Cloud Powered Interview Preparation Agent

PrepMate AI is a complete AI interview preparation web application for students and freshers. It generates personalized HR questions, technical questions, model answers, skill-gap analysis, and a 7-day learning roadmap using IBM watsonx.ai / IBM Granite.

## Problem Statement

Students often prepare for internships and placements using generic interview questions. They lack personalized guidance based on their resume, skills, projects, and target job role.

## Solution

PrepMate AI allows a user to paste their resume or skills, enter a target role, and generate a structured interview preparation report.

## Features

- Resume/skills input
- Target role input
- HR interview questions
- Technical interview questions
- Model answers
- Skill-gap analysis
- 7-day roadmap
- IBM Granite integration-ready
- Fallback demo mode when IBM credentials are not added
- FastAPI backend
- Responsive frontend
- Render deployment notes

## IBM Cloud Services Used

- IBM watsonx.ai
- IBM Granite Foundation Model

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- AI: IBM watsonx.ai Granite
- Deployment: GitHub + Render

## Folder Structure

```text
PrepMateAI_Complete_Working/
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
├── docs/
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

Backend URL:

```text
http://127.0.0.1:8000
```

## Run Frontend

Open:

```text
frontend/index.html
```

## API Endpoint

```text
POST /generate
```

Example request:

```json
{
  "resume_text": "Python, SQL, FastAPI, GitHub, ML projects",
  "target_role": "AI Engineer Intern"
}
```

## Environment Variables

Create `backend/.env` using `backend/.env.example`.

```text
IBM_API_KEY=your_key_here
IBM_PROJECT_ID=your_project_id_here
IBM_REGION=us-south
```

The app works in fallback demo mode even without IBM credentials.

## Author

Chhavi Khosla

# Deployment Guide

## Backend on Render

1. Push project to GitHub.
2. Go to Render.
3. Create New Web Service.
4. Connect GitHub repo.
5. Build command:

```bash
pip install -r requirements.txt
```

6. Start command:

```bash
cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

7. Add environment variables:
- IBM_API_KEY
- IBM_PROJECT_ID
- IBM_REGION

## Frontend

You can host frontend on:
- GitHub Pages
- Netlify
- Vercel

After backend deployment, update `API_URL` in `frontend/assets/js/app.js`.

# PrepMate AI Project Report

## Title
PrepMate AI – IBM Cloud Powered Interview Preparation Agent

## Problem
Students and freshers often depend on generic interview questions. This does not help them prepare according to their own resume, skills, or target role.

## Objective
To build an AI-powered interview preparation assistant that creates personalized preparation material.

## IBM Cloud Usage
The solution uses IBM watsonx.ai and IBM Granite model for generating interview reports.

## Methodology
1. User enters resume and target role.
2. Backend receives input using FastAPI.
3. Prompt builder creates a structured AI prompt.
4. IBM Granite generates the preparation report.
5. Frontend displays the result.

## Output
The system generates:
- HR interview questions
- Technical interview questions
- Model answers
- Skill-gap analysis
- 7-day roadmap

## Future Scope
- PDF resume upload
- Voice mock interview
- ATS score
- User login
- Saved history

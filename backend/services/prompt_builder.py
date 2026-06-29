from utils.helpers import clean_text

def build_interview_prompt(resume_text: str, target_role: str) -> str:
    resume_text = clean_text(resume_text)
    target_role = clean_text(target_role)

    return f'''
You are PrepMate AI, an intelligent interview preparation assistant for students and freshers.

Candidate Resume / Skills:
{resume_text}

Target Role:
{target_role}

Create a structured, practical interview preparation report with these exact sections:

1. Personalized Candidate Summary
2. HR Interview Questions
3. Technical Interview Questions
4. Strong Model Answers
5. Skill Gap Analysis
6. 7-Day Learning Roadmap
7. Final Confidence Tips

Make the output student-friendly, specific to the role, and useful for internship or entry-level interviews.
'''

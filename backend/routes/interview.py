from fastapi import APIRouter
from models.schemas import InterviewRequest, InterviewResponse
from services.prompt_builder import build_interview_prompt
from services.ibm_granite import generate_with_granite

router = APIRouter(tags=["Interview Preparation"])

@router.post("/generate", response_model=InterviewResponse)
def generate_interview_prep(request: InterviewRequest):
    prompt = build_interview_prompt(request.resume_text, request.target_role)

    try:
        result = generate_with_granite(prompt)
        return InterviewResponse(result=result, source="IBM Granite")
    except Exception as error:
        return InterviewResponse(
            result=generate_fallback_report(request.resume_text, request.target_role),
            source="Fallback demo response",
            note=f"IBM Granite not connected yet: {str(error)}"
        )

def generate_fallback_report(resume_text: str, target_role: str) -> str:
    return f'''
PrepMate AI Interview Preparation Report

Target Role: {target_role}

1. Personalized Candidate Summary
You are preparing for the {target_role} role. Your resume/skills show potential, and your preparation should focus on explaining your projects clearly, strengthening role-specific concepts, and improving confidence.

2. HR Interview Questions
- Tell me about yourself.
- Why are you interested in the {target_role} role?
- What are your strengths and weaknesses?
- Tell me about a project you are proud of.
- How do you handle deadlines or pressure?

3. Technical Interview Questions
- What are the most important skills for a {target_role}?
- Explain one project from your resume that is relevant to this role.
- What tools, frameworks, or libraries have you used?
- How would you solve a real-world problem related to this role?
- How do you debug or improve your work?

4. Strong Model Answer
I am a motivated student interested in {target_role}. I have been improving my skills through hands-on learning, projects, and continuous practice. I enjoy solving practical problems and I am ready to learn, contribute, and grow in a professional environment.

5. Skill Gap Analysis
Focus on:
- Stronger project explanation
- Role-specific technical basics
- GitHub and portfolio polish
- Communication confidence
- Practical implementation

6. 7-Day Learning Roadmap
Day 1: Revise basic concepts for {target_role}
Day 2: Prepare HR answers
Day 3: Practice technical questions
Day 4: Improve one project explanation
Day 5: Update GitHub and README
Day 6: Do a mock interview
Day 7: Final revision and confidence practice

7. Final Confidence Tips
Speak clearly, keep answers structured, and connect your skills to the target role. Be honest about what you know and show willingness to learn.
'''

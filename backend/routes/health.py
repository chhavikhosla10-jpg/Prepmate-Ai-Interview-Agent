from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "PrepMate AI Backend is running",
        "status": "success"
    }

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "PrepMate AI"
    }

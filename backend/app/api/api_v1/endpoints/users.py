from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def read_user_me():
    # TODO: Get current user profile
    pass

@router.put("/me")
def update_user_me():
    # TODO: Update user profile (college, course, etc.)
    pass

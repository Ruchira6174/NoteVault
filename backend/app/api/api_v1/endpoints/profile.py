from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.profile import ProfileCreate, ProfileUpdate, ProfileResponse, PublicCreatorProfile
from app.services.profile_service import ProfileService
from app.dependencies.auth import get_current_active_user
from app.models.user import User

router = APIRouter()

@router.get("/me", response_model=ProfileResponse)
async def get_my_profile(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Returns logged-in student's profile."""
    return ProfileService.get_my_profile(db, current_user.id)

@router.post("", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_profile(
    profile_in: ProfileCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Creates academic profile."""
    return ProfileService.create_profile(db, current_user.id, profile_in)

@router.patch("", response_model=ProfileResponse)
async def update_profile(
    profile_in: ProfileUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Updates profile."""
    return ProfileService.update_profile(db, current_user.id, profile_in)

@router.get("/creator/{username}", response_model=PublicCreatorProfile)
async def get_public_creator_profile(
    username: str,
    db: Session = Depends(get_db)
):
    """Returns public creator profile."""
    return ProfileService.get_public_creator_profile(db, username)

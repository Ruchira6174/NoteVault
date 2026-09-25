from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.models.user import User
from app.schemas.profile import ProfileCreate, ProfileUpdate

class ProfileService:
    @staticmethod
    def create_profile(db: Session, user_id: str, profile_in: ProfileCreate) -> Profile:
        existing_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if existing_profile:
            raise HTTPException(status_code=400, detail="Profile already exists for this user")
            
        db_profile = Profile(user_id=user_id, **profile_in.model_dump(exclude_unset=True))
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        return db_profile

    @staticmethod
    def update_profile(db: Session, user_id: str, profile_in: ProfileUpdate) -> Profile:
        db_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if not db_profile:
            raise HTTPException(status_code=404, detail="Profile not found")
            
        update_data = profile_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_profile, field, value)
            
        db.commit()
        db.refresh(db_profile)
        return db_profile

    @staticmethod
    def get_my_profile(db: Session, user_id: str) -> Profile:
        db_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if not db_profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        return db_profile

    @staticmethod
    def get_public_creator_profile(db: Session, username: str) -> Profile:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
            
        profile = db.query(Profile).filter(Profile.user_id == user.id).first()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
            
        return profile

    @staticmethod
    def upload_profile_photo_placeholder(db: Session, user_id: str, file_name: str) -> Profile:
        """Placeholder for cloud storage upload logic."""
        # TODO: Implement cloud storage upload and return URL
        photo_url = f"https://placeholder.com/{file_name}"
        
        db_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if not db_profile:
            raise HTTPException(status_code=404, detail="Profile not found")
            
        db_profile.profile_photo = photo_url
        db.commit()
        db.refresh(db_profile)
        return db_profile

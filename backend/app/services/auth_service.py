from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.models.user import User
from app.schemas.auth import UserRegister, UserLogin
from app.core.security import get_password_hash, verify_password
from app.core.jwt import create_access_token
from app.core.config import get_settings

settings = get_settings()

class AuthService:
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> User | None:
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def register_user(db: Session, user_in: UserRegister):
        if AuthService.get_user_by_email(db, user_in.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        if AuthService.get_user_by_username(db, user_in.username):
            raise HTTPException(status_code=400, detail="Username already registered")
            
        hashed_password = get_password_hash(user_in.password)
        db_user = User(
            email=user_in.email,
            username=user_in.username,
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(db_user.id)}, expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer", "user": db_user}

    @staticmethod
    def authenticate_user(db: Session, user_in: UserLogin):
        user = AuthService.get_user_by_email(db, user_in.email_or_username)
        if not user:
            user = AuthService.get_user_by_username(db, user_in.email_or_username)
            
        if not user or not verify_password(user_in.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email/username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}

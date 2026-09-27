# pyrefly: ignore [missing-import]
from fastapi import HTTPException, status
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import UserRegister, UserLogin
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token


class AuthService:
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def register_user(db: Session, user_in: UserRegister):
        # Check duplicate email
        if AuthService.get_user_by_email(db, user_in.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        # Check duplicate username
        if AuthService.get_user_by_username(db, user_in.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken",
            )

        # Create new user
        db_user = User(
            full_name=user_in.full_name,
            username=user_in.username,
            email=user_in.email,
            password_hash=hash_password(user_in.password),
            college=user_in.college,
            branch=user_in.branch,
            semester=user_in.semester,
            bio=user_in.bio,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        # Generate JWT
        access_token = create_access_token(str(db_user.id))

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": db_user,
        }

    @staticmethod
    def authenticate_user(db: Session, user_in: UserLogin):
        # Find by email first
        user = AuthService.get_user_by_email(db, user_in.email_or_username)

        # Otherwise find by username
        if not user:
            user = AuthService.get_user_by_username(
                db, user_in.email_or_username
            )

        # Verify credentials
        if not user or not verify_password(
            user_in.password, user.password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email/username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = create_access_token(str(user.id))

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }
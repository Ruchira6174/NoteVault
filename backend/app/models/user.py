import uuid
from datetime import datetime, timezone
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # One-to-one relationship with Profile
    profile: Mapped["Profile"] = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan")

import uuid
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, index=True, nullable=False)
    
    full_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    profile_photo: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    bio: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    college: Mapped[Optional[str]] = mapped_column(String(255), index=True, nullable=True)
    university: Mapped[Optional[str]] = mapped_column(String(255), index=True, nullable=True)
    course: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    branch: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    semester: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    joined_year: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    
    average_rating: Mapped[float] = mapped_column(Float, default=0.0)
    total_resources: Mapped[int] = mapped_column(Integer, default=0)
    total_sales: Mapped[int] = mapped_column(Integer, default=0)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationship to User
    user: Mapped["User"] = relationship("User", back_populates="profile")

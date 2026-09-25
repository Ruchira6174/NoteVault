import uuid
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import Integer, DateTime, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (UniqueConstraint("resource_id", "reviewer_id", name="uq_resource_reviewer"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    resource_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("resources.id", ondelete="CASCADE"), index=True, nullable=False)
    reviewer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    resource: Mapped["Resource"] = relationship("Resource", back_populates="reviews")
    reviewer: Mapped["User"] = relationship("User", foreign_keys=[reviewer_id])

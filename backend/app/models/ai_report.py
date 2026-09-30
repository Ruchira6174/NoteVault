from app.models.resource import Resource
import uuid
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import Integer, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class AIReport(Base):
    __tablename__ = "ai_reports"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    resource_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("resources.id", ondelete="CASCADE"), unique=True, index=True, nullable=False)
    
    accuracy_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    originality_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    readability_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    syllabus_coverage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    
    ai_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    plagiarism_percentage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    generated_quiz_count: Mapped[int] = mapped_column(Integer, default=0)
    
    verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    resource: Mapped["Resource"] = relationship("Resource", back_populates="ai_report")

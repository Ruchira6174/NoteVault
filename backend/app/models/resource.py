import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional, List
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, Text, Boolean, Numeric, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from app.core.database import Base
from app.core.constants import Visibility, ResourceStatus

class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    
    title: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    subject: Mapped[Optional[str]] = mapped_column(String(255), index=True, nullable=True)
    university: Mapped[Optional[str]] = mapped_column(String(255), index=True, nullable=True)
    course: Mapped[Optional[str]] = mapped_column(String(100), index=True, nullable=True)
    branch: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    semester: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    
    tags: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String), nullable=True)
    
    visibility: Mapped[Visibility] = mapped_column(SQLEnum(Visibility), default=Visibility.PRIVATE, index=True)
    is_paid: Mapped[bool] = mapped_column(Boolean, default=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.00)
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    
    average_rating: Mapped[float] = mapped_column(Float, default=0.0)
    downloads: Mapped[int] = mapped_column(Integer, default=0)
    views: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[ResourceStatus] = mapped_column(SQLEnum(ResourceStatus), default=ResourceStatus.PENDING, index=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    owner: Mapped["User"] = relationship("User", backref="resources")
    files: Mapped[List["ResourceFile"]] = relationship("ResourceFile", back_populates="resource", cascade="all, delete-orphan")
    ai_report: Mapped["AIReport"] = relationship("AIReport", back_populates="resource", uselist=False, cascade="all, delete-orphan")
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="resource", cascade="all, delete-orphan")
    access_requests: Mapped[List["AccessRequest"]] = relationship("AccessRequest", back_populates="resource", cascade="all, delete-orphan")
    purchases: Mapped[List["Purchase"]] = relationship("Purchase", back_populates="resource", cascade="all, delete-orphan")
    bookmarks: Mapped[List["Bookmark"]] = relationship("Bookmark", back_populates="resource", cascade="all, delete-orphan")

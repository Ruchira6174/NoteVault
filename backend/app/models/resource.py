import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum as SQLEnum,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import ARRAY, UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.constants import ResourceStatus, Visibility
from app.core.database import Base
from app.models.user import User


class Resource(Base):
    __tablename__ = "resources"

    # ==============================
    # Primary Key
    # ==============================

    id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )

    # ==============================
    # Ownership
    # ==============================

    owner_id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ==============================
    # Basic Resource Information
    # ==============================

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    subject: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    university: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    course: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    branch: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )

    semester: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
    )

    tags: Mapped[Optional[list[str]]] = mapped_column(
        ARRAY(String),
        nullable=True,
    )

    # ==============================
    # Visibility & Pricing
    # ==============================

    visibility: Mapped[Visibility] = mapped_column(
        SQLEnum(Visibility),
        default=Visibility.PRIVATE,
        index=True,
    )

    is_paid: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=Decimal("0.00"),
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        default="USD",
    )

    # ==============================
    # Statistics
    # ==============================

    average_rating: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    downloads: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    views: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    # ==============================
    # Resource Status
    # ==============================

    status: Mapped[ResourceStatus] = mapped_column(
        SQLEnum(ResourceStatus),
        default=ResourceStatus.PENDING,
        index=True,
    )

    # ==============================
    # Timestamps
    # ==============================

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # ==============================
    # Relationships
    # ==============================

    owner: Mapped["User"] = relationship(
        "User",
        backref="resources",
    )

    files: Mapped[list["ResourceFile"]] = relationship(
        "ResourceFile",
        back_populates="resource",
        cascade="all, delete-orphan",
    )
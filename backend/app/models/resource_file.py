import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ResourceFile(Base):
    __tablename__ = "resource_files"

    # ==============================
    # Primary Key
    # ==============================

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )

    # ==============================
    # Resource Reference
    # ==============================

    resource_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("resources.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ==============================
    # File URLs
    # ==============================

    original_file_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    preview_file_url: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )

    thumbnail_url: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )

    # ==============================
    # File Metadata
    # ==============================

    file_size: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
    )

    page_count: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
    )

    mime_type: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
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
    # Relationship
    # ==============================

    resource: Mapped["Resource"] = relationship(
        "Resource",
        back_populates="files",
    )
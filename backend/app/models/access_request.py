import uuid
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String, DateTime, ForeignKey, Text, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from app.core.constants import AccessRequestStatus

class AccessRequest(Base):
    __tablename__ = "access_requests"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    resource_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("resources.id", ondelete="CASCADE"), index=True, nullable=False)
    buyer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    
    status: Mapped[AccessRequestStatus] = mapped_column(SQLEnum(AccessRequestStatus), default=AccessRequestStatus.PENDING, index=True)
    request_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    owner_response: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    requested_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    responded_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    resource: Mapped["Resource"] = relationship("Resource", back_populates="access_requests")
    buyer: Mapped["User"] = relationship("User", foreign_keys=[buyer_id])
    owner: Mapped["User"] = relationship("User", foreign_keys=[owner_id])

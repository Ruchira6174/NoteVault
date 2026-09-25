import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional
from sqlalchemy import String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    resource_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("resources.id", ondelete="SET NULL"), index=True, nullable=True)
    buyer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    transaction_id: Mapped[Optional[str]] = mapped_column(String(255), unique=True, index=True, nullable=True)
    
    purchased_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    resource: Mapped["Resource"] = relationship("Resource", back_populates="purchases")
    buyer: Mapped["User"] = relationship("User", foreign_keys=[buyer_id])

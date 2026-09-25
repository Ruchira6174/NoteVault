import uuid
from datetime import datetime, timezone
from decimal import Decimal
from sqlalchemy import Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, index=True, nullable=False)
    
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.00)
    lifetime_earnings: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.00)
    total_sales: Mapped[int] = mapped_column(Integer, default=0)
    pending_balance: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.00)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user: Mapped["User"] = relationship("User", backref="wallet")
    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="wallet", cascade="all, delete-orphan")

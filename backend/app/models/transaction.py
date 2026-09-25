import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional
from sqlalchemy import String, DateTime, ForeignKey, Numeric, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from app.core.constants import TransactionType

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    wallet_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("wallets.id", ondelete="CASCADE"), index=True, nullable=False)
    purchase_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("purchases.id", ondelete="SET NULL"), index=True, nullable=True)
    
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    commission: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0.00)
    creator_earning: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    
    transaction_type: Mapped[TransactionType] = mapped_column(SQLEnum(TransactionType), index=True, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="COMPLETED", index=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    wallet: Mapped["Wallet"] = relationship("Wallet", back_populates="transactions")
    purchase: Mapped[Optional["Purchase"]] = relationship("Purchase")

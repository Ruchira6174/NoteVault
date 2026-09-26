import uuid
from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from app.core.constants import TransactionType


class WithdrawRequest(BaseModel):
    amount: Decimal = Field(..., gt=0)
    upi_id: str = Field(..., min_length=5, max_length=100)


class WalletResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    balance: Decimal
    lifetime_earnings: Decimal
    total_sales: int
    pending_balance: Decimal
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TransactionResponse(BaseModel):
    id: uuid.UUID
    wallet_id: uuid.UUID
    purchase_id: Optional[uuid.UUID]
    amount: Decimal
    commission: Decimal
    creator_earning: Decimal
    transaction_type: TransactionType
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class EarningsSummary(BaseModel):
    total_earned: Decimal
    this_month_earned: Decimal
    available_balance: Decimal
    pending_clearance: Decimal

    model_config = ConfigDict(from_attributes=True)

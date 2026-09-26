from datetime import datetime
from decimal import Decimal
from uuid import UUID

from app.schemas.wallet import (
    WalletResponse,
    TransactionResponse,
    WithdrawRequest,
)


async def get_wallet_details(current_user: dict) -> WalletResponse:
    """Temporary wallet implementation until DB integration."""
    user_id = UUID(current_user["id"]) if isinstance(current_user["id"], str) else current_user["id"]

    return WalletResponse(
        id=user_id,
        user_id=user_id,
        balance=Decimal("0.00"),
        lifetime_earnings=Decimal("0.00"),
        total_sales=0,
        pending_balance=Decimal("0.00"),
        updated_at=datetime.utcnow(),
    )


async def get_wallet_transactions(
    current_user: dict,
    page: int,
    page_size: int,
) -> list[TransactionResponse]:
    """Return empty transaction history."""
    return []


async def withdraw_funds(
    request: WithdrawRequest,
    current_user: dict,
) -> str:
    """Placeholder withdrawal request."""
    return f"Withdrawal request of ₹{request.amount} submitted successfully."
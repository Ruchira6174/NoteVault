# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, Query
from typing import List

from app.dependencies.auth import get_current_active_user
from app.schemas.wallet import (
    WalletResponse,
    TransactionResponse,
    WithdrawRequest,
)
from app.services.wallet_service import (
    get_wallet_details,
    get_wallet_transactions,
    withdraw_funds,
)

router = APIRouter()


@router.get("/wallet", response_model=WalletResponse)
async def wallet_details(
    current_user: dict = Depends(get_current_active_user),
):
    """Return current balance and earnings summary."""
    return await get_wallet_details(current_user)


@router.get("/wallet/transactions", response_model=List[TransactionResponse])
async def wallet_transactions(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    current_user: dict = Depends(get_current_active_user),
):
    """Paginated wallet transaction history."""
    return await get_wallet_transactions(current_user, page, page_size)


@router.post("/wallet/withdraw")
async def withdraw(
    request: WithdrawRequest,
    current_user: dict = Depends(get_current_active_user),
):
    """Placeholder for withdrawal request."""
    result = await withdraw_funds(request, current_user)
    return {"detail": result}
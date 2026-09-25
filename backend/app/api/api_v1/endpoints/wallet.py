from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from uuid import UUID

from app.api import deps
from app.schemas.wallet import WalletResponse, TransactionResponse, WithdrawRequest
from app.services.wallet_service import get_wallet_details, get_wallet_transactions, withdraw_funds

router = APIRouter()

@router.get('/wallet', response_model=WalletResponse)
async def wallet_details(current_user: dict = Depends(deps.get_current_user)):
    """Return current balance and earnings summary for the logged‑in creator"""
    return await get_wallet_details(current_user)

@router.get('/wallet/transactions', response_model=List[TransactionResponse])
async def wallet_transactions(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    current_user: dict = Depends(deps.get_current_user),
):
    """Paginated list of wallet transaction history"""
    return await get_wallet_transactions(current_user, page, page_size)

@router.post('/wallet/withdraw')
async def withdraw(request: WithdrawRequest, current_user: dict = Depends(deps.get_current_user)):
    """Placeholder for withdrawal request – implementation TBD"""
    result = await withdraw_funds(request, current_user)
    return {'detail': result}

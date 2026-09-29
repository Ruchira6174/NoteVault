from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from uuid import UUID

from app.api import deps
from app.schemas.purchase import PurchaseCreate, PurchaseResponse
# pyrefly: ignore [missing-import]
from app.services.purchase_service import create_purchase, get_my_purchases, get_purchase_by_id

router = APIRouter()

@router.post("/purchase/{resource_id}", response_model=PurchaseResponse)
async def purchase_resource(
    resource_id: UUID,
    purchase_in: PurchaseCreate = Depends(),
    current_user: dict = Depends(deps.get_current_user),
):
    """Create a purchase (or free acquisition) for a resource"""
    return await create_purchase(resource_id, purchase_in, current_user)

@router.get("/purchase/me", response_model=List[PurchaseResponse])
async def my_purchases(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    current_user: dict = Depends(deps.get_current_user),
):
    return await get_my_purchases(current_user, page, page_size)

@router.get("/purchase/{purchase_id}", response_model=PurchaseResponse)
async def get_purchase(
    purchase_id: UUID,
    current_user: dict = Depends(deps.get_current_user),
):
    purchase = await get_purchase_by_id(purchase_id, current_user)
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return purchase

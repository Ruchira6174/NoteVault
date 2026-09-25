from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from uuid import UUID

from app.api import deps
from app.schemas.access_request import AccessRequestCreate, AccessRequestResponse
from app.services.permission_service import create_access_request, get_incoming_requests, get_outgoing_requests, approve_request, reject_request

router = APIRouter()

@router.post("/requests", response_model=AccessRequestResponse)
async def create_request(request: AccessRequestCreate, current_user: dict = Depends(deps.get_current_user)):
    """Create an access request for a resource"""
    return await create_access_request(request, current_user)

@router.get("/requests/incoming", response_model=List[AccessRequestResponse])
async def incoming_requests(current_user: dict = Depends(deps.get_current_user)):
    """Owner view of incoming access requests"""
    return await get_incoming_requests(current_user)

@router.get("/requests/outgoing", response_model=List[AccessRequestResponse])
async def outgoing_requests(current_user: dict = Depends(deps.get_current_user)):
    """Buyer view of outgoing access requests"""
    return await get_outgoing_requests(current_user)

@router.patch("/requests/{request_id}/approve", response_model=AccessRequestResponse)
async def approve(request_id: UUID, current_user: dict = Depends(deps.get_current_user)):
    return await approve_request(request_id, current_user)

@router.patch("/requests/{request_id}/reject", response_model=AccessRequestResponse)
async def reject(request_id: UUID, current_user: dict = Depends(deps.get_current_user)):
    return await reject_request(request_id, current_user)

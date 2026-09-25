from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Dict, Any
from app.core.database import get_db
from app.dependencies.auth import get_current_active_user
from app.models.user import User
from app.schemas.ai_report import AIReportResponse
from app.services.ai_service import AIService

router = APIRouter()

@router.post("/verify/{resource_id}", response_model=AIReportResponse)
async def verify_resource(
    resource_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Trigger AI verification pipeline for a resource."""
    return AIService.verify_resource(db, resource_id)

@router.get("/report/{resource_id}", response_model=AIReportResponse)
async def get_ai_report(
    resource_id: UUID,
    db: Session = Depends(get_db)
):
    """Return the AI Quality Report."""
    return AIService.get_ai_report(db, resource_id)

@router.get("/quiz/{resource_id}")
async def get_quiz(
    resource_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Return the generated quiz for the resource."""
    return AIService.get_quiz(db, resource_id)

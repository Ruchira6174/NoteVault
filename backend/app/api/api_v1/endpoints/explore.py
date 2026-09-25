from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Optional
from uuid import UUID

from app.api import deps
from app.schemas.resource import ResourceCardResponse
from app.services.search_service import search_resources, explore_resources, get_trending_resources, get_recommended_resources

router = APIRouter()

@router.get("/explore", response_model=List[ResourceCardResponse])
async def explore(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    subject: Optional[str] = None,
    university: Optional[str] = None,
    course: Optional[str] = None,
    semester: Optional[int] = None,
    branch: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    visibility: Optional[str] = None,
    min_ai_score: Optional[float] = None,
    max_ai_score: Optional[float] = None,
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    sort: Optional[str] = Query("newest", regex="^(newest|rating|downloads|price|ai_score)$"),
):
    """Public marketplace explorer with pagination and filters."""
    resources = await explore_resources(
        page=page,
        page_size=page_size,
        filters={
            "subject": subject,
            "university": university,
            "course": course,
            "semester": semester,
            "branch": branch,
            "price_range": (min_price, max_price),
            "visibility": visibility,
            "ai_score_range": (min_ai_score, max_ai_score),
            "rating_range": (min_rating, max_rating),
        },
        sort=sort,
    )
    return resources

@router.get("/explore/trending", response_model=List[ResourceCardResponse])
async def trending(limit: int = Query(10, ge=1, le=50)):
    """Most viewed resources globally."""
    return await get_trending_resources(limit)

@router.get("/explore/recommended", response_model=List[ResourceCardResponse])
async def recommended(limit: int = Query(10, ge=1, le=50)):
    """Resources ordered by AI score (high to low)."""
    return await get_recommended_resources(limit)

@router.get("/search", response_model=List[ResourceCardResponse])
async def search(
    query: str = Query(..., min_length=1),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    filters: Optional[dict] = None,
    current_user: Optional[dict] = Depends(deps.get_current_user),
):
    """Semantic and keyword search across public resources."""
    return await search_resources(query, page, page_size, filters or {})

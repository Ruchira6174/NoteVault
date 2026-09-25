from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Optional
from uuid import UUID

from app.api import deps
from app.schemas.resource import ResourceCardResponse
from app.services.search_service import search_resources

router = APIRouter()

@router.get("/search", response_model=List[ResourceCardResponse])
async def search_resources_endpoint(
    query: str = Query(..., min_length=1),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    subject: Optional[str] = None,
    university: Optional[str] = None,
    course: Optional[str] = None,
    semester: Optional[int] = None,
    branch: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    current_user: Optional[dict] = Depends(deps.get_current_user),
):
    """Semantic and keyword search across public resources.
    Returns a list of resource cards matching the query and optional filters.
    """
    filters = {
        "subject": subject,
        "university": university,
        "course": course,
        "semester": semester,
        "branch": branch,
        "price_range": (min_price, max_price),
        "rating_range": (min_rating, max_rating),
    }
    return await search_resources(query, page, page_size, filters)

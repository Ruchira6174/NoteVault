from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from uuid import UUID

from app.api import deps
from app.schemas.review import ReviewCreate, ReviewUpdate, ReviewResponse
from app.services.review_service import (
    create_review,
    update_review,
    delete_review,
    get_reviews_by_resource,
)

router = APIRouter()

@router.post('/reviews', response_model=ReviewResponse)
async def post_review(review: ReviewCreate, current_user: dict = Depends(deps.get_current_user)):
    """Create a review for a purchased resource"""
    return await create_review(review, current_user)

@router.patch('/reviews/{review_id}', response_model=ReviewResponse)
async def patch_review(
    review_id: UUID,
    review_in: ReviewUpdate,
    current_user: dict = Depends(deps.get_current_user),
):
    return await update_review(review_id, review_in, current_user)

@router.delete('/reviews/{review_id}')
async def delete_review_endpoint(review_id: UUID, current_user: dict = Depends(deps.get_current_user)):
    await delete_review(review_id, current_user)
    return {'detail': 'Review deleted'}

@router.get('/reviews/resource/{resource_id}', response_model=List[ReviewResponse])
async def get_resource_reviews(
    resource_id: UUID,
    current_user: dict = Depends(deps.get_current_user),
):
    return await get_reviews_by_resource(resource_id, current_user)

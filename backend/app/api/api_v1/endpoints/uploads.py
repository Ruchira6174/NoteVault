from fastapi import APIRouter, Depends, UploadFile, File
from app.dependencies.auth import get_current_active_user
from app.models.user import User
from app.services.upload_service import UploadService
from app.schemas.upload import UploadResponse
from pydantic import BaseModel

router = APIRouter()

class ThumbnailResponse(BaseModel):
    url: str

@router.post("/file", response_model=UploadResponse)
async def upload_file(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_active_user)
):
    """Upload PDF or document."""
    return await UploadService.process_file_upload(file, current_user.id)

@router.post("/image", response_model=UploadResponse)
async def upload_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_active_user)
):
    """Upload handwritten images."""
    return await UploadService.process_image_upload(file, current_user.id)

@router.post("/thumbnail", response_model=ThumbnailResponse)
async def upload_thumbnail(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_active_user)
):
    """Upload optional thumbnail."""
    url = await UploadService.process_thumbnail_upload(file, current_user.id)
    return ThumbnailResponse(url=url)

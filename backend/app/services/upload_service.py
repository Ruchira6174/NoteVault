import uuid
from fastapi import UploadFile, HTTPException
from app.schemas.upload import UploadResponse
from app.storage.file_manager import FileManager
from app.utils.pdf import count_pages

ALLOWED_DOC_TYPES = {"application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/vnd.openxmlformats-officedocument.presentationml.presentation"}
ALLOWED_IMG_TYPES = {"image/png", "image/jpeg", "image/jpg"}
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB placeholder

class UploadService:
    @staticmethod
    async def process_file_upload(file: UploadFile, user_id: str) -> UploadResponse:
        """Process document uploads (PDF, DOCX, PPTX)."""
        if file.content_type not in ALLOWED_DOC_TYPES:
            raise HTTPException(status_code=400, detail="Unsupported document format")
        
        storage_path = FileManager.generate_storage_path(user_id, file.filename)
        url = await FileManager.save_file(file, storage_path)
        
        # Placeholder for page count extraction if PDF
        pages = count_pages("mock_path") if file.content_type == "application/pdf" else None
        
        return UploadResponse(
            upload_url=url,
            resource_file_id=uuid.uuid4(),  # Mock ID for now, will link to DB later
            filename=file.filename
        )

    @staticmethod
    async def process_image_upload(file: UploadFile, user_id: str) -> UploadResponse:
        """Process image uploads for handwritten notes."""
        if file.content_type not in ALLOWED_IMG_TYPES:
            raise HTTPException(status_code=400, detail="Unsupported image format")
            
        storage_path = FileManager.generate_storage_path(user_id, file.filename)
        url = await FileManager.save_file(file, storage_path)
        
        return UploadResponse(
            upload_url=url,
            resource_file_id=uuid.uuid4(),
            filename=file.filename
        )

    @staticmethod
    async def process_thumbnail_upload(file: UploadFile, user_id: str) -> str:
        """Upload a thumbnail image."""
        if file.content_type not in ALLOWED_IMG_TYPES:
            raise HTTPException(status_code=400, detail="Unsupported image format")
            
        storage_path = FileManager.generate_storage_path(user_id, f"thumb_{file.filename}")
        url = await FileManager.save_file(file, storage_path)
        return url

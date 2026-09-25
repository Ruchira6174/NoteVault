import uuid
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class FileUploadRequest(BaseModel):
    filename: str = Field(..., max_length=255)
    mime_type: str = Field(..., max_length=100)
    file_size: int = Field(..., gt=0)

class UploadResponse(BaseModel):
    upload_url: str
    resource_file_id: uuid.UUID
    filename: str
    
    model_config = ConfigDict(from_attributes=True)

class PreviewGenerationResponse(BaseModel):
    resource_id: uuid.UUID
    preview_url: str
    thumbnail_url: str
    page_count: Optional[int]
    
    model_config = ConfigDict(from_attributes=True)

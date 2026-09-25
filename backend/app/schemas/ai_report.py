import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class AIQualityBreakdown(BaseModel):
    accuracy_score: Optional[float] = Field(None, ge=0.0, le=100.0)
    originality_score: Optional[float] = Field(None, ge=0.0, le=100.0)
    readability_score: Optional[float] = Field(None, ge=0.0, le=100.0)
    syllabus_coverage: Optional[float] = Field(None, ge=0.0, le=100.0)
    plagiarism_percentage: Optional[float] = Field(None, ge=0.0, le=100.0)
    
    model_config = ConfigDict(from_attributes=True)

class AIReportResponse(AIQualityBreakdown):
    id: uuid.UUID
    resource_id: uuid.UUID
    ai_summary: Optional[str]
    verified_at: Optional[datetime]
    
    model_config = ConfigDict(from_attributes=True)

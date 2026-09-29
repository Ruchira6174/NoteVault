# pyrefly: ignore [missing-import]
from fastapi import APIRouter

router = APIRouter()

@router.post("/request")
def request_access():
    # TODO: Buyer requests access to a resource
    pass

@router.post("/{request_id}/approve")
def approve_access():
    # TODO: Owner approves access
    pass

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def browse_marketplace():
    # TODO: Return public and semi-private resources
    pass

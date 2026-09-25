from fastapi import APIRouter
from app.api.api_v1.endpoints import users, resources, marketplace, wallet, permissions

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(resources.router, prefix="/resources", tags=["resources"])
api_router.include_router(marketplace.router, prefix="/marketplace", tags=["marketplace"])
api_router.include_router(permissions.router, prefix="/permissions", tags=["permissions"])
api_router.include_router(wallet.router, prefix="/wallet", tags=["wallet"])

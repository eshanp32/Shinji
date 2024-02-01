from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Root"])
async def root():
    return {"message": "Konichiwa From Shinji!"}


@router.get("/health", tags=["Health Check"])
async def health():
    return {"status": "ok"}

from fastapi import APIRouter

rei_router = APIRouter()


@rei_router.get("/health")
async def health():
    return {"status": "Ayanami Rei Unit-00 active"}

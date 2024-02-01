from fastapi import APIRouter

asuka_router = APIRouter()


@asuka_router.get("/health")
async def health():
    return {"status": "Asuka Langley Soryu Unit-02 active"}

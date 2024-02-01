from fastapi import FastAPI
from services.Rei.rei_router import rei_router
from services.Asuka.asuka_router import asuka_router
from core.config import APP_ENV, APP_CONFIGS, SHOW_DOCS_ENVIRONMENT

app = FastAPI(**APP_CONFIGS)
if APP_ENV not in SHOW_DOCS_ENVIRONMENT:
    from mangum import Mangum

    handler = Mangum(app)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Konichiwa From Shinji!"}

@app.get("/health", tags=["Health Check"])
async def health():
    return {"status": "Ikari Shinji Unit-01 active"}


app.include_router(prefix = "/rei", router = rei_router, tags=["Rei"])
app.include_router(prefix = "/asuka", router = asuka_router, tags=["Asuka"])

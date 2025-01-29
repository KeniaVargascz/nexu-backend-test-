from fastapi import FastAPI
from app.routers.router import router as user_router

app = FastAPI()

# Include router
app.include_router(user_router, prefix="/api", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API!!"}
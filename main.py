from fastapi import FastAPI
from src.routers import channel as chanel_router
from src.routers import show as show_router
from src.routers import search as search_router


app = FastAPI()

@app.get('/', tags=['main'])
async def get_channels():
    return None
app.include_router(
    chanel_router.router
)
app.include_router(
    show_router.router
)
app.include_router(
    search_router.router
)
from fastapi import FastAPI
from DataBase_functions import get_channels_db
from src.routers import channel as chanel_router
from src.routers import show as show_router
from src.routers import search as search_router


app = FastAPI()


@app.get('/', tags=['main'])
async def get_channels():
    return [{'id': el[0], 'name': el[1], 'ico_path': f'images/{el[1].upper()}/Иконки/icon.jpg', 'live_url': el[3]} for el in get_channels_db()]

app.include_router(
    chanel_router.router
)
app.include_router(
    show_router.router
)
app.include_router(
    search_router.router
)
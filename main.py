from fastapi import FastAPI
from src.routers import chanel as chanel_router
from src.routers import show as show_router


app = FastAPI()

app.include_router = (
    chanel_router
)
app.include_router = (
    show_router
)

@app.get('/')
async def get_channels():
    pass
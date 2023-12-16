from fastapi import APIRouter, Depends


router = APIRouter(
    prefix='/search',
    tags=['search']
)

@router.get('/')
async def get_search_data():
    pass
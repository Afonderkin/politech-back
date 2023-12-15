from fastapi import APIRouter


router = APIRouter(
    prefix='/show',
    tags=['show']
)

@router.get('/')
async def get_shows():
    pass

@router.get('/{id}')
async def get_show(id):
    pass
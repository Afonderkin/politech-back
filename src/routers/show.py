from fastapi import APIRouter


router = APIRouter(
    prefix='/show',
    tags=['show']
)

@router.get('/{id}')
async def get_show(id):
    pass
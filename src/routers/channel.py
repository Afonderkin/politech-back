from fastapi import APIRouter


router = APIRouter(
    prefix='/chanel',
    tags=['chanel']
)

@router.get('/{id}')
async def get_channel(id: int):
    pass
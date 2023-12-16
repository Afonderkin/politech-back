from fastapi import APIRouter


router = APIRouter(
    prefix='/channel',
    tags=['channel']
)


@router.get('/{id}')
async def get_channel(id):
    return '/images/НТВ/Иконки/icon.jpg'
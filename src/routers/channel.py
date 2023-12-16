from fastapi import APIRouter
from DataBase_functions import get_channel_info


router = APIRouter(
    prefix='/channel',
    tags=['channel']
)


@router.get('/{id}')
async def get_channel(id, day):
    channel_info = get_channel_info(id, day)[0]
    programm_info = get_channel_info(id, day)[1]

    channel_info = [{'name': el[0], 'icopath': f'images/{el[0].upper()}/Иконки/icon.jpg', 'liveurl': el[2]} for el in channel_info]
    return [channel_info, programm_info]
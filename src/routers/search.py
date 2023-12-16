from fastapi import APIRouter

from DataBase_functions import find_somethink


router = APIRouter(
    prefix='/search',
    tags=['search']
)


@router.get('/')
async def get_search_data(search_data, on_day, client_time):
    channels = find_somethink(search_data, on_day, client_time)[0]
    channels = {'channels': [{'id': el[0], 'name': el[1], 'iso_path': f'images/{el[1].upper()}/Иконки/icon.jpg', 'livepath': el[2]} for el in channels]}
    if len(channels['channels']) == 0:
        channels['channels'] = None
    programms = find_somethink(search_data, on_day, client_time)[1]
    programms = {'programms': [{'id': el[0], 'name': el[1]} for el in programms]}
    if len(programms['programms']) == 0:
        programms['programms'] = None
    return [channels, programms]


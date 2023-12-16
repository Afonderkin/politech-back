from fastapi import APIRouter

from DataBase_functions import get_programm_db

router = APIRouter(
    prefix='/show',
    tags=['show']
)


@router.get('/{id}')
async def get_show(id: int):
    programm_info = get_programm_db(id)
    return {"name_programm": programm_info[0], "Desc": programm_info[1], "channel_id": programm_info[2],
<<<<<<< HEAD
            "Tags": programm_info[3], 'ico-path': f'images/Иконки_телепередач/Иконки_Телепередачи_{programm_info[2]}/{programm_info[0]}/icon.jpg'}
=======
            "Tags": programm_info[3]}
>>>>>>> 89f7fe3b5563a67da520c14693e9f084ec3d0571

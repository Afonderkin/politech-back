from fastapi import APIRouter, Depends


router = APIRouter(
    prefix='/search',
    tags=['search']
)


@router.get('/')
async def get_search_data(search_data: str):
    return [{'name': search_data, 'ico-src': f'{search_data.upper()}/Иконки/icon.jpg'}]
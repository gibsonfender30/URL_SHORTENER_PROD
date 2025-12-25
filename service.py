from database.crud import add_slug_to_database, get_long_url_by_slug_from_databse
from exceptions import NoLongUrlFoundError
from shortener import generate_random_slug


async def generate_short_url(
        long_url: str,
) -> str:
    # 1 генерим slug
    # 2 добавляем в базу
    # 3 отдаем клиенту 
    slug = generate_random_slug()
    await add_slug_to_database(
        slug, long_url
    )
    return slug


async def get_url_by_slug(slug: str) -> str:
    long_url = await get_long_url_by_slug_from_databse(slug)
    if not long_url:
        raise NoLongUrlFoundError
    return long_url

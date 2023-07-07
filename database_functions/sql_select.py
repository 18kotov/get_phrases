from settings import get_logger
from database_functions.commucation_with_db import get_data

logger = get_logger(__name__)


@get_data
def get_phrases_russian_key(x: str) -> list:
    phrases = f"SELECT answer FROM english WHERE ask ILIKE '%{x}%';"
    return phrases


if __name__ == '__main__':
    x = 'где'
    print(get_phrases_russian_key(x))
    pass

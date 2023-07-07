from typing import List
from database_functions.sql_select import get_phrases_russian_key
from settings import get_logger

logger = get_logger(__name__)


def get_list_phrases(key: str) -> List[str]:
    list_tuple = get_phrases_russian_key(key)
    list_phrases = []
    if list_tuple is None:
        return list_phrases
    for x in list_tuple:
        list_phrases.append(x[0])

    return list_phrases


if __name__ == "__main__":
    pass

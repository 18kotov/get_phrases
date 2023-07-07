import re
from settings import get_logger


logger = get_logger(__name__)

def check_english_phrase(phrase: str) -> bool:
    status = False
    if len(phrase) == 0:
        return status
    if re.search('[а-яА-Я-0-9]', phrase):
        return status
    status = True
    return status


def check_russian_phrase(phrase: str) -> bool:
    status = False
    if len(phrase) == 0:
        return status
    if re.search('[a-zA-Z-0-9]', phrase):
        return status
    status = True
    return status


if __name__ == '__main__':
    pass
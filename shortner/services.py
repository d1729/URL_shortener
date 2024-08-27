import logging
import string
import random

from shortner.models import ShortUrl

log = logging.getLogger(__name__)

def generate_short_code():
    allowed_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(allowed_chars) for _ in range(8))


def generate_unique_short_code():
    short_code = generate_short_code()
    is_short_code_present = ShortUrl.objects.filter(short_code=short_code).exists()
    while is_short_code_present:
        short_code = generate_short_code()
    return short_code


def get_original_url(short_code):
    res = ShortUrl.objects.filter(short_code=short_code)
    if len(res) == 0:
        return None
    return res[0].original_url


def get_url_object(short_code):
    try:
        return ShortUrl.objects.get(short_code=short_code)
    except ShortUrl.DoesNotExist:
        log.error(f'Shorturl not found for {short_code}')
        return None

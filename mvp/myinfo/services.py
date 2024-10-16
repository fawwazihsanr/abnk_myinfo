import logging

from django.conf import settings
from django.utils.crypto import get_random_string

from mvp.myinfo.clients import MyInfoPersonalClientV4
from mvp.myinfo.constants import CALLBACK_URL
import redis

redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True
)

log = logging.getLogger(__name__)
client = MyInfoPersonalClientV4()


def retrieve_authorise_url(cookie):
    state = get_random_string(length=16)
    authorise_url = client.get_authorise_url(state, CALLBACK_URL)
    redis_client.set(f'user-{cookie}', state)
    return authorise_url


def get_auth_code(cookie, auth_code):
    oauth_state = redis_client.get(f'user-{cookie}')
    if not oauth_state:
        log.error(f"Oauth state not found for sessionid {cookie}")
        return "Oauth state not found."
    return client.retrieve_resource(auth_code, oauth_state, CALLBACK_URL)

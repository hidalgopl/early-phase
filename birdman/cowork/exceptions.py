from rest_framework import status
from rest_framework.exceptions import APIException


class NoPeerParameter(APIException):
    default_code = 'error'
    default_detail = 'You should include ?peer_pin=<peer_id>&user_pin=<user_id> arguments in URL!'
    status_code = status.HTTP_400_BAD_REQUEST


class BufferNotFound(APIException):
    default_code = 'error'
    default_detail = 'User or peer does not have availability!'
    status_code = status.HTTP_404_NOT_FOUND

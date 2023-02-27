from rest_framework.exceptions import APIException
from rest_framework import status

class TweetNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = 'error'
    default_detail = ('Tweet does not exist')

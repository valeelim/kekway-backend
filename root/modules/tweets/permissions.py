from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException

from root.modules.tweets.exceptions import TweetNotFoundException
from root.modules.accounts.models import UserAccount
from root.modules.tweets.models import Tweet

import root.modules.accounts.utils as utils


class IsTweetOwner(BasePermission, APIException):
    def has_permission(self, request, view):
        user_id = utils.get_user_id_by_request(request)
        user = UserAccount.objects.get(id=user_id)
        try:
            tweet = Tweet.objects.get(id=request.data.get('tweet_id'))
        except Tweet.DoesNotExist as e:
            raise TweetNotFoundException
        if user.role == 'Admin':
            return True
        return Tweet.objects.filter(owner=user_id).exists()
        
        
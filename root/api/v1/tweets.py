from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from root.services import tweet_service, account_service
from root.modules.tweets.serializers import TweetSerializer
from root.modules.tweets.permissions import IsTweetOwner
from root.modules.tweets.models import Tweet

import root.modules.accounts.utils as utils


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_tweet(request):
    tweet_dict = request.data
    if not tweet_dict.get('desc'):
        return JsonResponse(
            data={
                'message': 'Tweet must have a description'
            },
            safe=False,
            status=400
        )
    
    user_id = utils.get_user_id_by_request(request)
    tweet = tweet_service.create_tweet(user_id, tweet_dict)
    serializer = TweetSerializer(tweet, many=False)
    return JsonResponse(
        data=serializer.data,
        status=200
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_my_tweets(request):
    user_id = utils.get_user_id_by_request(request)
    tweets = tweet_service.get_my_tweets(user_id)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )


@api_view(["GET"])
@permission_classes([])
def get_user_tweets(request, username):
    try:
        target = account_service.get_user_by_username(username)
    except UserAccount.DoesNotExist as e:
        return JsonResponse(
            data={
                'message': str(e)
            },
            status=404
        )
    
    user_id = utils.get_user_id_by_request(request)
    tweets = tweet_service.get_user_tweets(user_id, target.id)
    serializer = TweetSerializer(tweets, many=True)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )


@api_view(["GET"])
@permission_classes([])
def get_all_valid_tweets(request):
    user_id = utils.get_user_id_by_request(request)
    tweets = tweet_service.get_all_valid_tweets(user_id)
    serializer = TweetSerializer(tweets, many=True)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsTweetOwner])
def edit_tweet(request):
    tweet_dict = request.data
    tweet = tweet_service.edit_tweet(tweet_dict)
    serializer = TweetSerializer(tweet, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=True,
        status=200
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsTweetOwner])
def delete_tweet(request):
    tweet_id = request.data.get('tweet_id')
    tweet_service.delete_tweet(tweet_id)
    return JsonResponse(
        data={
            'message': 'Tweet deleted successfully'
        },
        status=200
    )

    
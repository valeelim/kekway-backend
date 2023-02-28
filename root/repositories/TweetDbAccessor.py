from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from root.repositories.BaseDbAccessor import BaseDbAccessor
from root.modules.accounts.models import UserCloseFriendRelation
from root.modules.tweets.models import Tweet


class TweetDbAccessor(BaseDbAccessor):
    def create_tweet(self, user_id, tweet_dict):
        new_tweet = Tweet.objects.create(
            desc=tweet_dict.get('desc'),
            close_only=tweet_dict.get('close_only'),
            owner_id=user_id,
        )
        new_tweet.save()
        return new_tweet

    
    def get_my_tweets(self, user_id):
        return Tweet.objects.filter(owner=user_id).order_by('-created_at')


    def get_all_valid_tweets(self, user_id):
        close_with_owner = UserCloseFriendRelation.objects.filter(friended=user_id)\
            .values_list('friender', flat=True)
        return Tweet.objects.filter(
            Q(owner__in=close_with_owner) | 
            Q(close_only=False) | 
            Q(owner=user_id)
        ).order_by('-created_at')


    def get_user_tweets(self, user_id, target_id):
        if user_id == target_id or \
            UserCloseFriendRelation.objects.filter(friender=target_id, friended=user_id).exists():
            return Tweet.objects.filter(owner=target_id).order_by('-created_at')
        return Tweet.objects.filter(Q(owner=target_id) & Q(close_only=False)).order_by('-created_at')


    def edit_tweet(self, tweet_dict):
        if tweet_dict.get('desc') is None:
            raise ValueError('Tweet must have a description')
        
        tweet = Tweet.objects.get(id=tweet_dict.get('tweet_id'))
        tweet.desc = tweet_dict.get('desc')
        tweet.close_only = tweet_dict.get('close_only')

        tweet.save()
        return tweet


    def delete_tweet(self, tweet_id):
        return Tweet.objects.get(id=tweet_id).delete()

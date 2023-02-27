from django.urls import include, path
from root.api.v1 import tweets

urlpatterns = [
    path('create-tweet/', tweets.create_tweet),
    path('get-all-valid-tweets/', tweets.get_all_valid_tweets),
    path('get-user-tweets/<str:username>/', tweets.get_user_tweets),
    path('get-my-tweets/', tweets.get_my_tweets),
    path('edit-tweet/', tweets.edit_tweet),
    path('delete-tweet/', tweets.delete_tweet),
]
from root.repositories.TweetDbAccessor import TweetDbAccessor


class TweetService:
    def __init__(self, *args, **kwargs):
        self.db_accessor = TweetDbAccessor()

    def create_tweet(self, user_id, tweet_dict):
        return self.db_accessor.create_tweet(user_id, tweet_dict)

    def get_all_valid_tweets(self, user_id):
        return self.db_accessor.get_all_valid_tweets(user_id)

    def get_user_tweets(self, user_id, target_id):
        return self.db_accessor.get_user_tweets(user_id, target_id)

    def get_my_tweets(self, user_id):
        return self.db_accessor.get_my_tweets(user_id);

    def edit_tweet(self, tweet_dict):
        return self.db_accessor.edit_tweet(tweet_dict)

    def delete_tweet(self, tweet_id):
        return self.db_accessor.delete_tweet(tweet_id)
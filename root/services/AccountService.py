from root.repositories.AccountDbAccessor import AccountDbAccessor

from root.modules.accounts.serializers import UserOnlyIdAndNameAndUsername, UserSerializer

class AccountService:
    def __init__(self, *args, **kwargs):
        self.db_accessor = AccountDbAccessor()

    def edit_biodata(self, user_id, bio_data):
        return self.db_accessor.edit_biodata(user_id, bio_data)

    def get_user_by_username(self, username):
        return self.db_accessor.get_user_by_username(username)

    def get_user_by_id(self, user_id):
        return self.db_accessor.get_user_by_id(user_id)

    def upload_profile_photo(self, user_id, photo):
        self.db_accessor.upload_profile_photo(user_id, photo)

    def make_close_friend(self, friender_id, friended_id):
        self.db_accessor.make_close_friend(friender_id, friended_id)

    def get_users_by_substring(self, filter):
        return self.db_accessor.get_users_by_substring(filter);

    def edit_background_picture(self, user_id, photo):
        self.db_accessor.edit_background_picture(user_id, photo);

    # KINDA BAD
    def get_close_friend(self, user_id):
        relations = self.db_accessor.get_close_friend(user_id)
        result = []
        for rel in relations:
            serializer = UserSerializer(rel.friended, many=False)
            result.append({
                'user': serializer.data
            })
        return result

    def remove_close_friend(self, friender_id, friended_id):
        self.db_accessor.remove_close_friend(friender_id, friended_id)



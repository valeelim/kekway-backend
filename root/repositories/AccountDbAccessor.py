from root.repositories.BaseDbAccessor import BaseDbAccessor

from django.db.models import Q

from cloudinary import uploader
from root.modules.accounts.models import UserAccount, UserCloseFriendRelation

class AccountDbAccessor(BaseDbAccessor):
    def edit_biodata(self, user_id, biodata):
        try:
            user = UserAccount.objects.get(id=user_id)

            if biodata.get('email') is not None:
                user.email = biodata.get('email')

            if biodata.get('name') is not None:
                user.name = biodata.get('name')

            if biodata.get('username') is not None:
                user.username = biodata.get('username')

            if biodata.get('bio') is  not None:
                user.bio = biodata.get('bio')
            
            user.save()
            return user
        except Exception as e:
            raise e


    def upload_profile_photo(self, user_id, photo):
        user = UserAccount.objects.get(id=user_id)
        res = uploader.upload(photo, folder='/tweet')
        user.profile_photo = res.get('public_id')

        user.save()

    
    def get_user_by_username(self, username):
        try:
            return UserAccount.objects.get(username=username)
        except UserAccount.DoesNotExist as e:
            raise e

    
    def get_user_by_id(self, user_id):
        try:
            return UserAccount.objects.get(id=user_id);
        except UserAccount.DoesNotExist as e:
            raise e

    
    def get_users_by_substring(self, filter):
        users = UserAccount.objects.filter(
            Q(username__icontains=filter) | Q(name__icontains=filter))
        return users

    
    def edit_background_picture(self, user_id, photo):
        user = UserAccount.objects.get(id=user_id)
        res = uploader.upload(photo, folder='/tweet')
        user.background_photo = res.get('public_id')

        user.save()


    def make_close_friend(self, friender_id, friended_id):
        if friended_id == friender_id:
            raise ValueError('You cannot befriend yourself')
        existing_relations = UserCloseFriendRelation.objects.filter(
            friender=friender_id, friended=friended_id)
        if existing_relations.exists():
            raise ValueError('User is already a close friend')
        return UserCloseFriendRelation.objects.create(
            friender_id=friender_id, friended_id=friended_id
        )


    def get_close_friend(self, user_id):
        return UserCloseFriendRelation.objects.filter(friender=user_id)

    
    def remove_close_friend(self, friender_id, friended_id):
        if friended_id == friender_id:
            raise ValueError('You cannot unfriend yourself')
        existing_relations = UserCloseFriendRelation.objects.filter(
            friender=friender_id, friended=friended_id
        )
        if not existing_relations.exists():
            raise ValueError('User was never a close friend')
        return UserCloseFriendRelation.objects.get(
            friender=friender_id, friended=friended_id
        ).delete()




    
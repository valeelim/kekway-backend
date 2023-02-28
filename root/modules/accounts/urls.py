from django.urls import include, path
from root.api.v1 import accounts

urlpatterns = [
    path('logout/', accounts.logout),

    path('me/', accounts.me),
    path('edit-biodata/', accounts.edit_biodata),
    path('upload-profile-photo/', accounts.upload_profile_photo),
    path('edit-background-picture/', accounts.edit_background_picture),

    path('make-close-friend/', accounts.make_close_friend),
    path('get-close-friend/', accounts.get_close_friend),
    path('remove-close-friend/', accounts.remove_close_friend),

    path('get-user-by-username/<str:username>/', accounts.get_user_by_username),
    path('get-user-by-id/<int:user_id>/', accounts.get_user_by_id),
    path('get-users-by-substring', accounts.get_users_by_substring),
]
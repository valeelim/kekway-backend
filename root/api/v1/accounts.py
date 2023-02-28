from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from root.services import account_service
from root.modules.accounts.models import UserAccount
from root.modules.accounts.serializers import UserSerializer

import root.modules.accounts.utils as utils

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    user_id = utils.get_user_id_by_request(request)
    user = account_service.get_user_by_id(user_id)
    serializer = UserSerializer(user, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=True,
        status=200
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    return JsonResponse(
        data={
            'message': 'Successfully logged out.',
        },
        status=200
    )

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_background_picture(request):
    photo = request.data.get('photo')
    user_id = utils.get_user_id_by_request(request)
    account_service.edit_background_picture(user_id, photo)
    return JsonResponse(
        data={
            'message': 'Background photo successfully changed'
        },
        status=200
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_biodata(request):
    user_id = utils.get_user_id_by_request(request)
    try:
        user = account_service.edit_biodata(user_id, request.data)
        serializer = UserSerializer(user, many=False)
        return JsonResponse(
            data=serializer.data,
            status=200
        )
    except (UserAccount.DoesNotExist, Exception) as e:
        return JsonResponse(
            data={
                'message': str(e)
            },
            status=404
        )

@api_view(["GET"])
@permission_classes([])
def get_user_by_id(request, user_id):
    try:
        user = account_service.get_user_by_id(user_id)
        serializer = UserSerializer(user, many=False)
        return JsonResponse(
            data=serializer.data,
            status=200
        )
    except UserAccount.DoesNotExist as e:
        return JsonResponse(
            data={
                'message': str(e),
            },
            status=404
        )

@api_view(["GET"])
@permission_classes([])
def get_user_by_username(request, username):
    try:
        user = account_service.get_user_by_username(username)
        serializer = UserSerializer(user, many=False)
        return JsonResponse(
            data=serializer.data,
            status=200
        )
    except UserAccount.DoesNotExist as e:
        return JsonResponse(
            data={
                'message': str(e)
            },
            status=404
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_profile_photo(request):
    photo = request.data.get('photo')
    user_id = utils.get_user_id_by_request(request)
    account_service.upload_profile_photo(user_id, photo)
    return JsonResponse(
        data={
            'message': 'Profile photo successfully changed'
        },
        status=200
    )

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def make_close_friend(request):
    friender_id = utils.get_user_id_by_request(request)
    friended_id = request.data.get('friended_id')
    if friended_id is None:
        return JsonResponse(
            data={
                'message': 'Friend id is required'
            },
            status=400
        )
    try:
        account_service.make_close_friend(friender_id, friended_id)
        return JsonResponse(
            data={
                'message': 'Successfully made a new close friend'
            },
            status=200
        )
    except ValueError as e:
        return JsonResponse(
            data={
                'message': str(e)
            },
            status=400,
        )

@api_view(["GET"])
@permission_classes([])
def get_users_by_substring(request):
    params = request.GET
    filter = params.get('filter')
    users = account_service.get_users_by_substring(filter)
    serializer = UserSerializer(users, many=True)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_close_friend(request):
    user_id = utils.get_user_id_by_request(request)
    close_friends = account_service.get_close_friend(user_id)
    return JsonResponse(
        data=close_friends,
        safe=False,
        status=200
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_close_friend(request):
    friender_id = utils.get_user_id_by_request(request)
    friended_id = request.data.get('friended_id')
    if friended_id is None:
        return JsonResponse(
            data={
                'message': 'Friend id is required'
            },
            status=400
        )
    try:
        account_service.remove_close_friend(friender_id, friended_id)
        return JsonResponse(
            data={
                'message': 'User successfully unfriended'
            },
            safe=True,
            status=200
        )
    except ValueError as e:
        return JsonResponse(
            data={
                'message': str(e)
            },
            status=400
        )


    

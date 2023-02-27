import jwt

from django.conf import settings
from root.modules.accounts.models import UserAccount

jwt_decode_cache = {}

def get_user_id_by_request(request):
    if request.user.is_anonymous:
        return None
    access_token = request.headers.get('Authorization')[4:]
    if not access_token in jwt_decode_cache.keys():
        jwt_decode_cache[access_token] = jwt.decode(access_token, options={"verify_signature": False}).get('user_id')
    return jwt_decode_cache[access_token]
    

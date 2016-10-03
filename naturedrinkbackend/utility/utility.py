from rest_framework import status
from rest_framework.response import Response

def anonymous(req) :
    if req.user.is_anonymous :
        content = {'ERROR_MESSEGE': 'User is unauthorized.'}
        return Response(content,status=status.HTTP_401_UNAUTHORIZED)

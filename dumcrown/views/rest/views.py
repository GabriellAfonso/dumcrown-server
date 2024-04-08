from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from dumcrown.serializers import UserSerializer
import jwt
from django.conf import settings


class LoginRest(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)

        payload = {'user_id': user.id}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        serializer = UserSerializer(user)
        return Response({'token': token, 'user': serializer.data})

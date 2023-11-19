from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import User, CustomAccountAdapter
from .serializers import CustomRegisterSerializer, UserCustomSerializer
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


# Create your views here.
@api_view(['GET', 'PUT'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def userdetail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'GET':
        serializer = UserCustomSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if request.user.id == user.id:
            serializer = UserCustomSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({'message':'권한이 없습니다.'})
# -*- coding: utf-8 -*-
from django.contrib.auth import login, logout

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..core.models import CustomUser, Job
from .authenticators import QuietBasicAuthentication
from .permissions import IsOwner, IsStaffOrTargetUser
from .serializers import JobSerializer, UserSerializer


class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response()


class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)


class UserList(generics.ListCreateAPIView):
    model = CustomUser
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDetail(generics.RetrieveAPIView):
    model = CustomUser
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsStaffOrTargetUser,)


class UserPostList(generics.ListAPIView):
    model = Job
    serializer_class = JobSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(user__username=self.kwargs.get('username'))


class PostList(generics.ListAPIView):
    model = Job
    serializer_class = JobSerializer
    permission_classes = (IsStaffOrTargetUser,)

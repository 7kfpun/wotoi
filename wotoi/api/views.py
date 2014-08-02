# -*- coding: utf-8 -*-
from django.contrib.auth import login, logout

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from ..core.models import CustomUser, Job, Language
from .authenticators import QuietBasicAuthentication
from .permissions import IsOwner  # , IsStaffOrTargetUser
from .serializers import (
    JobSerializer,
    LanguageSerializer,
    UserDetailSerializer,
    UserSerializer,
)


class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response()


class UserList(generics.ListCreateAPIView):
    model = CustomUser
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDetail(generics.RetrieveAPIView):
    model = CustomUser
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    # permission_classes = (IsStaffOrTargetUser,)
    permission_classes = (IsAuthenticated,)


class UserJobList(generics.ListAPIView):
    model = Job
    serializer_class = JobSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        queryset = super(UserJobList, self).get_queryset()
        return queryset.filter(user__username=self.kwargs.get('username'))


class JobList(generics.ListAPIView):
    model = Job
    serializer_class = JobSerializer
    # permission_classes = (IsStaffOrTargetUser,)
    permission_classes = (IsAuthenticated,)


class LanguageList(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.filter(alpha2__isnull=False)

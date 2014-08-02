# -*- coding: utf-8 -*-

from rest_framework import serializers
from ..core.models import CustomUser, Job


# class CustomUserSerializer(serializers.Serializer):
    # pk = serializers.Field()  # Note: `Field` is an untyped read-only field.

    # username = serializers.CharField(max_length=256)
    # user_type = serializers.ChoiceField(
        # choices=CustomUser.USER_TYPE, required=False)

    # description = serializers.CharField(max_length=256, required=False)
    # url = serializers.CharField(max_length=256, required=False)
    # phone = serializers.CharField(max_length=256, required=False)

    # def restore_object(self, attrs, instance=None):
        # if instance:
            # # Update existing instance
            # instance.username = attrs.get('username', instance.username)
            # instance.user_type = attrs.get('user_type', instance.user_type)
            # instance.description = attrs.get(
                # 'description', instance.description)
            # instance.url = attrs.get('url', instance.url)
            # instance.phone = attrs.get('phone', instance.phone)
            # return instance

        # # Create new instance
        # return CustomUser(**attrs)

    # class Meta:
        # model = CustomUser


class UserSerializer(serializers.ModelSerializer):

    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'first_name',
                  'last_name', 'email')
        read_only_fields = ('id',)
        write_only_fields = ('password',)


class JobSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.

    # title = serializers.CharField(max_length=256)
    # category = serializers.ChoiceField(
    # choices=Job.CATEGORY_TYPE, required=False)
    # description = serializers.CharField(max_length=256, required=False)
    # price = serializers.CharField(max_length=256, required=False)
    # unit = serializers.ChoiceField(choices=Job.CATEGORY_TYPE, required=False)
    # until_date = serializers.CharField(max_length=256, required=False)

    class Meta:
        model = Job
        fields = ('pk', 'title', 'category', 'description', 'price', 'unit',
                  'until_date')

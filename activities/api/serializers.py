from django.contrib.auth import get_user_model
from rest_framework import serializers

from events.models import Events
from user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UserActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class EventsListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)

    class Meta:
        model = Events
        fields = ["name", "meeting_time", "description", "user"]
        read_only_fields = ["user"]


class OneEventSerializer(EventsListSerializer):  # просмотр участников события
    users = serializers.ListSerializer(child=UserListSerializer(), read_only=True)


class OneUserSerializer(UserListSerializer):  # просмотр событий, на которые подписан
    events = serializers.ListSerializer(child=EventsListSerializer(), read_only=True)

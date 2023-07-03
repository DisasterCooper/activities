from rest_framework.response import Response
from rest_framework import generics, mixins, status, permissions

from . import serializers
from events.models import Events
from user.models import User
from .serializers import UserRegisterSerializer, UserListSerializer
from .permissions import IsSuperUserOrOnlyRead


class EventsListAPIView(generics.ListAPIView):  # +
    queryset = Events.objects.all()
    serializer_class = serializers.EventsListSerializer


class OneEventAPIView(generics.GenericAPIView):
    queryset = Events.objects.all()
    lookup_url_kwarg = "events_id"
    lookup_field = "meeting_time"
    serializer_class = serializers.OneEventSerializer


class UserRegisterAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserActiveSerializer
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListWatchAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsSuperUserOrOnlyRead]


class OneUserAPIView(generics.GenericAPIView):
    pass

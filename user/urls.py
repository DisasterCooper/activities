from django.urls import path

from activities.api import views

# /api/users/

app_name = 'user'

urlpatterns = [
    path("register", views.UserRegisterAPIView.as_view(), name='registration'),
    path("", views.UserListWatchAPIView.as_view(), name='user-list'),
    path("<int:user_id>", views.OneUserAPIView.as_view()),
]

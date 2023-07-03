from django.urls import path

from activities.api import views

# /api/events/

app_name = 'events'

urlpatterns = [
    path("", views.EventsListAPIView.as_view()),
    path("<int:event_id>", views.OneEventAPIView.as_view()),
]

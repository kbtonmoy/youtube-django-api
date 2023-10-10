from django.urls import path
from .views import TranscriptView

urlpatterns = [
    path('transcript/<str:video_id>/', TranscriptView.as_view(), name='transcript'),
]

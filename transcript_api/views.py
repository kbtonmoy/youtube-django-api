from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle  # Import ScopedRateThrottle
from youtube_transcript_api import YouTubeTranscriptApi

class TranscriptView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]  # Apply ScopedRateThrottle
    throttle_scope = 'custom'  # Use the custom throttle rate

    def get(self, request, video_id, *args, **kwargs):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return Response(transcript, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

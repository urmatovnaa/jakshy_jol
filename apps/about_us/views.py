from rest_framework.viewsets import ModelViewSet

from apps.about_us.models import Video, WhatsApp
from apps.about_us.serializers import VideoSerializer, WhatsAppSerializer


class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class WhatsAppView(ModelViewSet):
    queryset = WhatsApp.objects.all()
    serializer_class = WhatsAppSerializer

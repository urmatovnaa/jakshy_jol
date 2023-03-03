from rest_framework import serializers

from apps.about_us.models import Video, WhatsApp


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['url_video', 'title']


class WhatsAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsApp
        fields = ['url_video']

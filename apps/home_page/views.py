from rest_framework.viewsets import ModelViewSet

from apps.home_page.models import Review
from apps.home_page.serializers import ReviewSerializer


class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


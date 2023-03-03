from django.urls import path

from apps.home_page.views import ReviewView


urlpatterns = [
    path('reviews/', ReviewView.as_view({'get': 'list'})),
]


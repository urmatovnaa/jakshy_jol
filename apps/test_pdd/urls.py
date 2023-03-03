from django.urls import path

from apps.test_pdd.views import TestView, AnswerView

urlpatterns = [
    path('', TestView.as_view({'get': 'list'})),
    path('<int:pk>/', AnswerView.as_view({'get': 'list'})),
]

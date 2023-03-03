from rest_framework.viewsets import ModelViewSet

from apps.test_pdd.models import Test, Answer
from apps.test_pdd.serializers import TestSerializer, TestANSSerializer, AnswerSerializer

from rest_framework.response import Response


class TestView(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class AnswerView(ModelViewSet):
    queryset = None
    serializer_class = TestSerializer
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        id_t = self.kwargs.get('pk')
        correct_ans = Answer.objects.filter(test=id_t).filter(is_correct=True)
        test = Test.objects.filter(id=id_t)
        data = {
            'test': TestANSSerializer(test, context=context, many=True).data,
            'answer': AnswerSerializer(correct_ans, context=context, many=True).data,
        }
        return Response(data)

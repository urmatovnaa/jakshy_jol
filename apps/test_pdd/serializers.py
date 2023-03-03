from rest_framework import serializers

from apps.test_pdd.models import Test, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'test', 'answer', 'is_correct']


class TestSerializer(serializers.ModelSerializer):
    test = AnswerSerializer(many=True)

    class Meta:
        model = Test
        fields = ['id', 'question', 'photo', 'test']


class TestANSSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'explanation']


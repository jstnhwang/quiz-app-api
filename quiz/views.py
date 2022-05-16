from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import QuizSerializer
from .models import Quiz


class QuizView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all quizzes.
        """
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return JsonResponse(serializer.data, safe=False)

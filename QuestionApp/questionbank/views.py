from questionbank.models import Questions, Category
from questionbank.serializers import QuestionSerializer, CategoryListSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class QuestionList(generics.ListCreateAPIView):
    """
    List all questions, or create a new question.
    """
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    paginate_by = 10
    def get_queryset(self):
        return Questions.objects.all().order_by('number')

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List indivdual question, or updates a question.
    """
    model = Questions
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return Questions.objects.filter(id=self.kwargs['id'])
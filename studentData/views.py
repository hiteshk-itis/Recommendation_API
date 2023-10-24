from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StdLogViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.StdLog.objects.all().order_by('student_id')
    serializer_class = serializers.StdLogSerializer


class StdQuizViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.StdQuiz.objects.all().order_by('student_id')
    serializer_class = serializers.StdQuizSerializer


class StdAssignmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.StdAssignment.objects.all().order_by('student_id')
    serializer_class = serializers.StdAssignmentSerializer
from rest_framework import serializers
from . import models


class StdAssignmentSerializer(serializers.HyperlinkedModelSerializer): 
    student_id = serializers.ReadOnlyField()
    class Meta: 
        model = models.StdAssignment
        fields = '__all__'

class StdLogSerializer(serializers.HyperlinkedModelSerializer): 
    student_id = serializers.ReadOnlyField()
    class Meta: 
        model = models.StdLog
        fields = '__all__'

class StdQuizSerializer(serializers.HyperlinkedModelSerializer): 
    student_id = serializers.ReadOnlyField()
    class Meta: 
        model = models.StdQuiz
        fields = '__all__'
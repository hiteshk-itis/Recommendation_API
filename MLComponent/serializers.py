from rest_framework import serializers
from .models import ContentBasedFinalDf 

class ContentBasedFinalDfSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = ContentBasedFinalDf
        fields = "__all__"
        

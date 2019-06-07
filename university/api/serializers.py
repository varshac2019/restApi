from rest_framework import serializers
from university.models import University,ProgramHighlight

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'



class ProgramHighlightSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    class Meta:
        model = ProgramHighlight
        fields = '__all__'

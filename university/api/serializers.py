from rest_framework import serializers
from university.models import University,ProgramHighlight

class ProgramHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramHighlight
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    program_highlights  = ProgramHighlightSerializer()
    class Meta:
        model = University
        fields = '__all__'





from rest_framework import generics
from .serializers import UniversitySerializer,ProgramHighlightSerializer
from university.models import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UniversityAPIDetailView(generics.RetrieveAPIView, generics.ListAPIView):
    serializer_class = UniversitySerializer
    #lookup_field     ='id'
    queryset   = University.objects.all()

#    def get_detail(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



'''
class UniversityModelListAPIView(viewsets.ViewSet):
    def list(self, request):
        queryset = University.objects.all()
        serializer = UniversitySerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = ProgramHighlight.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProgramHighlightSerializer(user)     
        return Response(serializer.data)
'''

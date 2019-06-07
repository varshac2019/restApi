from rest_framework import generics
from .serializers import UniversitySerializer,ProgramHighlightSerializer
from university.models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
'''
class UniversityAPIDetailView(generics.RetrieveAPIView, generics.ListAPIView):
    serializer_class = UniversitySerializer
    queryset   = University.objects.all()

    def get_detail(self, request, *args, **kwargs):
         return self.retrieve(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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


class UniversityModelViewset(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset   = University.objects.all()
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('name','city','location','rank')
    search_fields = ('name','city','location','rank')
    

#    def get_queryset(self):
#        request = self.request
#        qs = University.objects.all()
#        query = request.GET.get('q')

#        if query is not None:
#            qs = qs.filter(name__icontains=query)
#        return qs

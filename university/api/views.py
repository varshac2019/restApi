from rest_framework import generics,permissions
from .serializers import UniversitySerializer,ProgramHighlightSerializer
from university.models import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters


class CustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
        return False


    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
        return False


class UniversityModelViewset(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset   = University.objects.all()
    permission_classes = (CustomPermission,)
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('name','city','location','rank')
    search_fields = ('name','city','location','rank')

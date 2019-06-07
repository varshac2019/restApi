from django.conf.urls import url
from .views import *

urlpatterns = [
#    url(r'^$', UniversityModelListAPIView.as_view({'get': 'list'})),
#    url(r'^$', UniversityModelListAPIView.as_view()),
#    url(r'^(?P<pk>\d+)/$', UniversityModelListAPIView.as_view({'get': 'retrieve'}),name='detail'),


#    url(r'^$', UniversityAPIDetailView.as_view()),
#    url(r'^(?P<pk>\d+)/$', UniversityAPIDetailView.as_view())


    url(r'^$', UniversityModelViewset.as_view({'get':'list'})),
]


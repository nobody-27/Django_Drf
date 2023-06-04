from django.shortcuts import render
from rest_framework import viewsets
from Nested_Serializer_Exmp.models import Profile
from Nested_Serializer_Exmp.serializer import ProfileSerializer
# Create your views here.

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get','post','retrieve','put','patch']
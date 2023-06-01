from django.shortcuts import render
from Authtication_Token.models import Token
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from Authtication_Token.serializers import TokenSerializer
# Create your views here.


class TokenModelViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
from rest_framework import serializers
from Authtication_Token.models import Token

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['id','name','age','bio']
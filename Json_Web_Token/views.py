from django.shortcuts import render
from Json_Web_Token.models import Student_data
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from Json_Web_Token.serializers import Student_Serializer_Json
# Create your views here.


class Student_class(GenericAPIView):
    serializer_class = Student_Serializer_Json
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        data = Student_data.objects.all()
        serilizer = self.serializer_class(data,many=True)
        print(serilizer.data,"data")
        return Response({"status": "success", "data": serilizer.data, "code": status.HTTP_200_OK})
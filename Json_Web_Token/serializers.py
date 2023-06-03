
from Json_Web_Token.models import Student_data
from rest_framework import serializers

class Student_Serializer_Json(serializers.ModelSerializer):
    class Meta:
        model = Student_data
        fields = '__all__'
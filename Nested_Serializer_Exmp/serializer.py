from rest_framework import serializers
from Nested_Serializer_Exmp.models import Profile,Hobby
from rest_framework.parsers import FormParser, MultiPartParser
class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user_hobby = HobbySerializer(many=True,read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        profile_instance = Profile.objects.create(**validated_data)
        Hobby.objects.create(user=profile_instance)
        return profile_instance

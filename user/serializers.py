from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import UserModel

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['password'] = user.password
        return token

class SignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        password =user.password
        user.set_password(password)
        user.is_active =True
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = "__all__"
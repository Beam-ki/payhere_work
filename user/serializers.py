from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import UserModel
from user.validators import email_validator, password_check_validator, password_vaildator

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['password'] = user.password
        return token

class SignUpSerializer(serializers.ModelSerializer):
    def validate(self, attrs):

        if attrs["email"].replace(" ", "") != "":
            valid_email = email_validator(attrs["email"])
            if valid_email == False:
                raise serializers.ValidationError({"message":"이메일 형식이 아닙니다!"})

        if attrs["password"].replace(" ", "") =="" or attrs["password_check"].replace(" ", "") == "":
            raise serializers.ValidationError({"message":"비밀번호는 공백일 수 없습니다!"})

        if attrs["password"] != "" and attrs["password_check"] != "":
            valid_password = password_vaildator(attrs["password"], attrs["password_check"])
            valid_password2 = password_check_validator(attrs["password"], attrs["password_check"])

            if valid_password == False:
                raise serializers.ValidationError({"message":"비밀번호는 8자 이상, 특수문자(@!%*#?&)를 하나 이상, 숫자를 하나 이상 포함해야 합니다!"})
            elif valid_password2 == False:
                raise serializers.ValidationError({"message":"비밀번호가 다릅니다"})

        attrs.pop("password_check", None)
        return super().validate(attrs)
    
    def create(self, validated_data):
        email = super().create(validated_data)
        password =email.password
        email.set_password(password)
        email.is_active =True
        email.save()
        return email

    class Meta:
        model = UserModel
        fields = "__all__"
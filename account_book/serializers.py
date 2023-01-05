from rest_framework import serializers
from account_book.models import account_book
from user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields=("email",)

class account_bookSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = account_book
        fields = "__all__"
        
class account_book_Create_Serializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) # 유저 정보를 가져온다 !
    class Meta:
        model=account_book
        fields = "__all__"
from django.shortcuts import render
from rest_framework.views import APIView
from user.serializers import SignUpSerializer
from .models import UserModel
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class UsertokenSerializer(APIView):
    pass
class Signup(APIView):
    def post(self, request):
        print("asd")
        serializer = SignUpSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print("asd2")
            serializer.save()
            return Response({"message":"회원가입이 되었습니다!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"회원가입이 실패했습니다!"}, status=status.HTTP_400_BAD_REQUEST)
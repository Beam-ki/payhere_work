from django.shortcuts import render
from rest_framework.views import APIView
from user.serializers import SignUpSerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import UserModel
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class Signup(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"회원가입이 되었습니다!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"회원가입이 실패했습니다!"}, status=status.HTTP_400_BAD_REQUEST)
        
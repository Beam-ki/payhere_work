from django.shortcuts import render
from rest_framework.views import APIView
from account_book.serializers import account_bookSerializer,account_book_Create_Serializer
from .models import account_book
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
# Create your views here.

class account_bookCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        serializer = account_book_Create_Serializer(data=request.data)
        print(request.user)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({"data": serializer.data, "message": "생성이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class account_bookView(APIView):

    def get(self, request):
        account_book_id = int(request.GET.get('account_book_id', None))
        Account_book = get_object_or_404(account_book, id=account_book_id)
        serializer = account_book_Create_Serializer(Account_book)
        return Response({"products":serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request):
        account_book_id = int(request.GET.get('account_book_id', None))
        Account_book = get_object_or_404(account_book, id=account_book_id)
        serializer = account_bookSerializer(Account_book, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정되었습니다.", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.error})

    def delete(self, request):
        account_book_id = int(request.GET.get('account_book_id', None))
        Account_book = get_object_or_404(account_book, id=account_book_id)
        Account_book.delete()
        return Response({"message":"게시글이 삭제 되었습니다."}, status=status.HTTP_200_OK)
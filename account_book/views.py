from django.shortcuts import render
from rest_framework.views import APIView
from account_book.serializers import account_bookSerializer,account_book_Create_Serializer
from .models import account_book
from rest_framework.response import Response
from rest_framework import status, permissions
from .pagination import PageNumberPagination, get_pagination_result
from rest_framework.generics import get_object_or_404
# Create your views here.
class accout_book_view(APIView):
    def get(self, request):
        
        account_books = account_book.objects.filter().order_by('-created_at')
        account_books1= account_books.order_by('-id')
        paginator = PageNumberPagination()
        p = paginator.paginate_queryset(queryset=account_books1, request=request)
        paging = get_pagination_result(paginator, account_books1.count())
        serializer = account_bookSerializer(p, many=True)
        return Response({"data": serializer.data, "page":paging}, status=status.HTTP_200_OK)
    
class account_bookCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self, request):
        serializer = account_book_Create_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            print(request.user)
            return Response({"data": serializer.data, "message": "생성이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class account_bookView(APIView):
    
    def get(self, request):
        account_book_id = int(request.GET.get('account_book_id', None))
        Account_book = get_object_or_404(account_book, id=account_book_id)
        serializer = account_book_Create_Serializer(Account_book)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)   
    
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
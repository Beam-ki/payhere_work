from django.urls import path
from account_book import views
# Create your views here.

urlpatterns=[
    path('create/',views.account_bookCreateView.as_view()),
    path('view/',views.account_bookView.as_view()),

]

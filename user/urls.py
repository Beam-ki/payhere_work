from django.urls import path
from user import views
# Create your views here.

urlpatterns=[
    path("login/", views.MyTokenObtainPairSerializer.as_view(),name="login"),
    path("signup/", views.Signup.as_view(), name="signup"),

]

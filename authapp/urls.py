from django.urls import path
from .views import home, login, register

app_name = "authapp"
urlpatterns = [
    path("", home, name="home"),
    path("user/login/", login, name="login"),
    path("user/register/", register, name="register")
]

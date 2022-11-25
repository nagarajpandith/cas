from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.register, name="register"),
]

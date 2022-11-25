from django.urls import path
from . import views
from django.templatetags.static import static 
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path('favicon.ico', RedirectView.as_view(url=static('favicon.ico'))),
]

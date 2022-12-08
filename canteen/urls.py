from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.register, name="register"),
    path("addItems/", views.addItems, name="addItems"),
    path("updateItem/<int:itemNo>", views.updateItem, name="updateItem"),
    path("deleteItem/<int:itemNo>", views.deleteItem, name="deleteItem"),
    path("items/", views.items, name="items"),
]+  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

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
    path("order/", views.order, name="order"),
    path("viewOrders/", views.viewOrders, name="viewOrders"),
    path("markCompleted/", views.markCompleted, name="markCompleted"),
    path("billing/<int:tokenNo>", views.billing, name="billing"), 
    path("summary", views.summary, name="summary"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

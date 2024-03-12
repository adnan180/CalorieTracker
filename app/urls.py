from django.urls import path
from app.views import FoodList, FoodRegister, FoodRemove, FoodUpdate, FoodDetail
from . import views as v

urlpatterns = [
    path("", v.index, name="index"),
    path("FoodList/", FoodList.as_view(), name="FoodList"),
    path("FoodRegister/", FoodRegister.as_view(), name="FoodRegister"),
    path("FoodRemove/<int:pk>", FoodRemove.as_view(), name="FoodRemove"),
    path("FoodUpdate/<int:pk>", FoodUpdate.as_view(), name="FoodUpdate"),
    path("FoodDetail/<int:pk>", FoodDetail.as_view(), name="FoodDetail"),
    path("signin/", v.signin, name="signin"),
    path("signup/", v.signup, name="signup"),
    path("userlogout/", v.userlogout, name="userlogout"),
    path('foodadd/', v.foodadd, name="foodadd"),
]

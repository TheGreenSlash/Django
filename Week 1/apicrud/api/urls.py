from django.urls import path
from .views import getUsers , createUser, userDetail



urlpatterns = [
    path('users/', getUsers, name="get-users"),
    path('users/create/', createUser, name="create-user"),
    path('users/<int:pk>/', userDetail, name="user-detail")
]
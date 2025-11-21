from django.urls import path
from . import views


urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='create-blog'),
    path('blogposts/<int:pk>/', views.BlogPostListUpdateDelete.as_view(), name='update')
]
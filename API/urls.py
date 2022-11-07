from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsViewSet.as_view()),
    path('posts/<int:pk>', views.DetailPostViewSet.as_view()),
]
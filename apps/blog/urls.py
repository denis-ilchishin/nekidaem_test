from django.urls import include, path

from .views import BlogDetail, BlogsList

urlpatterns = [
    path('', BlogsList.as_view(), name='blog-list'),
    path('<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
]

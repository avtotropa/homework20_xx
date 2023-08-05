from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogCreateView, BlogListView, BlogDetailView, BloUpdateView, BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='blogs'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('update/<int:pk>/', BloUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]

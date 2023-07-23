from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostDetailView, BlogPostListView

app_name = BlogConfig.name

urlpatterns = [
    path('catalog/<int:pk>/', BlogPostDetailView.as_view(), name='test'),
    path('blog/publ', BlogPostListView.as_view(), name='publ')
]

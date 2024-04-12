from django.urls import path
from blogs.views import BlogListAPIView, BlogDetailAPIView, BlogReviewListCreateAPIView, BlogReviewDetailAPIView
app_name = 'blogs'

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog-list'),
    path('<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('blogreviews/', BlogReviewListCreateAPIView.as_view(), name='blog-review-list'),
    path('blogreviews/<int:pk>/', BlogReviewDetailAPIView.as_view(), name='blog-review-detail'),
]

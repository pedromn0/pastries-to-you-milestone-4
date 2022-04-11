from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('blog_detail/<int:post_id>', views.blog_detail, name='blog_detail'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('blog_detail/<int:post_id>', views.blog_detail, name='blog_detail'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>', views.delete_post, name='delete_post'),
]

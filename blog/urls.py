from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>', views.blog_post, name="blog_post")
]

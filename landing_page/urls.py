from django.urls import path
from landing_page import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('cv/', views.cv, name='cv')
]

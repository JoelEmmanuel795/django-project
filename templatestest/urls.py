from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
#    path('menu/', views.menu),
    path('menu_card/', views.menu_by_id),
]
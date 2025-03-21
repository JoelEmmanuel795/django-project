from django.urls import path
from . import views

urlpatterns = [
    path('say_hello/', views.say_hello),
    path('homepage/', views.homepage),
    path('display_date/', views.display_date),
    path('menu/', views.menu),
    path('testing/', views.testing),
    path('testing2', views.testing2),
    path('testing3', views.testing3),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path('dishes/<str:dish>', views.menuitems)
]
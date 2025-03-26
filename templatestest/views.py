from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse

# Create your views here.

# def about(request):
#     about_content = {'about': "This is the about page for the Little Lemon website."}
#     return render(request, 'about.html', about_content)

# def menu(request):
#     newmenu = {'mains': [
#         {'name': 'Greek Salad', 'price': 10.00},
#         {'name': 'Pasta Carbonara', 'price': 12.00},
#         {'name': 'Chicken Marsala', 'price': 15.00},
#         {'name': 'Beef Wellington', 'price': 20.00},
#     ]}
#     return render(request, 'menu.html', newmenu)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World!")

def homepage(request):
    return HttpResponse("Welcome to the Little Lemon restaurant!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon again!</h1>"""
    return HttpResponse(text)

def testing(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 

def testing2(request): 
    path = request.path
    response = HttpResponse("This")
    return HttpResponse(path, content_type='text/html', charset='utf-8') 

def testing3(request): 
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""<br>
    <br>Path: {path}
    <br>Address: {address}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>User agent: {user_agent}
    <br>Path info: {path_info}
    <br>Response header: {response.headers}
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is yummy esp. with Pesto!',
        'falafel': 'Falafel is kinda yummy when prepared right',
        'cheesecake': 'OMG, cheesecake is the bestttt!!'
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)
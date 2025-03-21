from django.shortcuts import render

# Create your views here.
def about(request):
    about_content = {'about': "This is the about page for the Little Lemon website."}
    return render(request, 'about.html', about_content)
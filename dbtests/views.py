from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# from dbtests.forms import InputForm
from dbtests.forms import LogForm

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'home.html', context)
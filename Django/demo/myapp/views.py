from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {'todos': items})

def contact(request):
    return render(request, "contact.html")

from .forms import OrderForm

def create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form submitted successfully!")
    else:
        form = OrderForm()

    return render(request, "create.html", {'form': form})
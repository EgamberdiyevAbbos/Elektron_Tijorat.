from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def category(request):
    category = Category.objects.all()
    return render(request, 'category.html', )

def customer(request):
    customer = Customer.objects.all()
    return render(request, 'customer.html', )

def product(request):
    product = Product.objects.all()
    return render(request, 'product.html',) 

def buy(request):
    buy = Buy.objects.all()
    return render(request, 'buy.html', ) 

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        product = Product.objects.filter(Q(name__icontains=q) | Q(price__icontains=q) | Q(category__name__icontains=q))
    else:
        product = Product.objects.all().order_by('-id')

    context = {
        'product': product,
        'q': q,
    }
    return render(request, 'search.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
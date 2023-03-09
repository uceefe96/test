from django.shortcuts import render
from .forms import LoginForm
from .models import Login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

@login_required
def about(request):
    if request.method == 'POST':
        dataform = LoginForm(request.POST)
        if dataform.is_valid():
            dataform.save()
    

    
    
    # cne = request.POST.get('cne')
    # cin = request.POST.get('cin')
    # data = Login(cne=cne, cin=cin)
    # data.save()

    return render(request, 'guichet/about.html')
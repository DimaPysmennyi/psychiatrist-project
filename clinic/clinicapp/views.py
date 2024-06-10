from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.

def faq_view(request):
    return render(request, 'clinicapp/faq.html')

def main_view(request):
    return render(request, 'clinicapp/main.html')

def contacts_view(request):
    return render(request, 'clinicapp/contacts.html')

def form_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(**form.cleaned_data)
            form = UserForm(request.POST, instance=user)
            form.save()
            return redirect("form") 
    else:
        form = UserForm()
    return render(request, 'clinicapp/form.html', context={'form': form})

def services_view(request):
    return render(request, 'clinicapp/services.html')

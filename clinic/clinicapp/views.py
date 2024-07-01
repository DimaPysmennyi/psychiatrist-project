from django.shortcuts import render, redirect
from django.http import JsonResponse
# from asyncio import create_task
from .forms import UserForm
from .models import User
from .bot import main
import asyncio

# Create your views here.

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 

def main_view(request):
    return render(request, 'clinicapp/main.html')

def contacts_view(request):
    return render(request, 'clinicapp/contacts.html')

def form_view(request):
    form = UserForm()
    # print(form)
    return render(request, 'clinicapp/form.html', context={'form': form})

def services_view(request):
    return render(request, 'clinicapp/services.html')

def about_view(request):
    return render(request, 'clinicapp/about.html')

def handle_form_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(**form.cleaned_data)
            form = UserForm(request.POST, instance=user)
            form.save()
            text = f"Новий запис! \n{request.POST.get('first-name')} {request.POST.get('surname')} \n{request.POST.get('phone')} \n{request.POST.get('email')} \nКоментар: {request.POST.get('comment')}"

            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

            asyncio.create_task(main(text, -4210991870))
            return JsonResponse({"message": "Форму було надіслано!"})

        else:
            return JsonResponse({"message": "Неправильно заповнені поля!", "status": 403})
    # else:
        # return render(request, 'clinicapp/form.html', request={"form": form})   
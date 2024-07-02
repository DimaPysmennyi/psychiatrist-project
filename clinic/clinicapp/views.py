from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import EmailMessage
# from asyncio import create_task
from .forms import UserForm
from .models import User
from clinic.settings import DEFAULT_FROM_EMAIL, EMAIL_HOST_USER


# Create your views here.

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 

def main_view(request):
    return render(request, 'clinicapp/main.html')

def contacts_view(request):
    return render(request, 'clinicapp/contacts.html')

def form_view(request):
    form = UserForm()
    # print(form)
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
            text = f"Новий запис! \n{request.POST.get('name')} {request.POST.get('surname')} \n{request.POST.get('phone')} \n{request.POST.get('email')} \nКоментар: {request.POST.get('comment')}"

            message = EmailMessage(
                subject = "Новий запис!",
                body = f"Новий запис!\n{text}",
                from_email = DEFAULT_FROM_EMAIL,
                to = ["communityservine@gmail.com"]
            )
            message.send()

            return JsonResponse({"message": "Форму було надіслано!"})

        else:
            return JsonResponse({"message": "Неправильно заповнені поля!", "status": 403})
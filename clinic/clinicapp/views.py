from django.shortcuts import render, redirect
from validate_email import validate_email
from phone_number_validator.validator import PhoneNumberValidator


def validate_email_address(value):
    email = validate_email(value, verify=True)
    if email == False:
        return False
    
def validate_phone_number(value):
    validator = PhoneNumberValidator(api_key='num_live_ROMrNcOIBkh4nuVGQCy5i5qqsBNbXZGTdcdKLrw4')
    if not validator.validate(value):
        return False



#Імпорт класу JsonResponse
from django.http import JsonResponse

#Імпорт класу EmailMessage для створення повідомлення на email
from django.core.mail import EmailMessage

# Імпорт форми UserForm
from .forms import UserForm

# Імпорт моделі User
from .models import User

# Імпорт константи DEFAULT_FROM_EMAIL, в якій міститься адреса відправника email
from clinic.settings import DEFAULT_FROM_EMAIL


# Функція відображення файлу main.html
def main_view(request):
    return render(request, 'clinicapp/main.html')

# Функція відображення файлу contacts.html
def contacts_view(request):
    return render(request, 'clinicapp/contacts.html')

# Функція відображення файлу form.html
def form_view(request):
    # Отримуємо форму з forms.py
    form = UserForm()
    return render(request, 'clinicapp/form.html', context={'form': form})

# Функція відображення файлу services.html
def services_view(request):
    return render(request, 'clinicapp/services.html')


# Функція відображення файлу about.html
def about_view(request):
    return render(request, 'clinicapp/about.html')


# Функція для приймання запиту після відправки форми
def handle_form_request(request):
    if request.method == "POST":
        # Отримуємо дані користувача із форми
        form = UserForm(request.POST)
        # Якщо форма правильно заповнена:
        if form.is_valid():
            # Заносимо дані користувача у модель User
            form = UserForm(request.POST, instance=user)

            if validate_email_address(form.data["email"]) == False:
                return JsonResponse({"message": "Не дійсний e-mail!"})

            if validate_email_address(form.data["phone"]) == False:
                return JsonResponse({"message": "Не дійсний номер телефону!"})

            user = User.objects.create(**form.cleaned_data)

            # Зберігаємо форму 
            form.save()

            # Створюємо змінну із текстом для відправки повідомлення на пошту
            text = f"Новий запис! \n{request.POST.get('name')} {request.POST.get('surname')} \n{request.POST.get('phone')} \n{request.POST.get('email')} \nКоментар: {request.POST.get('comment')}"

            # Об'єкт класу повідомлення
            message = EmailMessage(
                subject = "Новий запис!", # тема
                body = text, # текст повідомлення
                from_email = DEFAULT_FROM_EMAIL, # відправник
                to = ["communityservine@gmail.com"] # кому
            )

            # Відправка повідомлення
            message.send()

            # Повертається Json-відповідь до клієнта
            return JsonResponse({"message": "Форму було надіслано!"})

        # Якщо форма неправильна:
        else:
            # Повертається Json-відповідь до клієнта із помилкою
            return JsonResponse({"message": "Неправильно заповнені поля!", "status": 403})
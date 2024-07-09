# Веб-сайт приватної практики психолога Ярослави Тимченко

### Учасники команди:
* Письменний Дмитро (Team Lead):\
<https://github.com/DimaPysmennyi>
* Погрібняк Никита:\
<https://github.com/nikitos881>
* Валерій Глазунов:\
<https://github.com/ValeraGlazunov>

Проект складається з 5 веб-сторінок (головна, послуги, про мене, контакти, форма для запису на консультацію). На кожній сторінці можна знайти потрібну інформацію про Ярославу Тимченко та її послуги у сфері психології.

![2024](https://github.com/DimaPysmennyi/psychiatrist-project/assets/90316617/5e9c89bc-97ea-4a56-ac40-eae42fc5c5cc)

## Чому проект корисний?

Наш проект пов'язаний із наданням людям необхідної психологічної допомоги, тому він є дуже корисним для оточуючих. 
____

## Як приступити до роботи з проектом?
### Перелік та опис кожного модуля, який має бути встановленим:
* **Django** - Python-фреймворк, на якому побудований цей веб-сайт.

* Модулі які потрібні для роботи з номерами телефонів:
    * **phonenumbers**
    * **django-phonenumber-field**
    * **django-phonenumbers**
    * **phonenumber-number-validator**

* **validate_email** - модуль, який потрібен для валідації e-mail.
    * **py3dns** - залежність від validate_email.

### Як запустити проект локально?
1. Встановити усі зазначені вище модулі.
2. Склонувати репозиторій проекту (`git clone https://github.com/DimaPysmennyi/psychiatrist-project.git`).
3. Перейти в директорію clinic.
4. Провести міграції (`python manage.py migrate`).
5. Запустити локальний сервер (`python manage.py runserver [порт]`).

[Посилання на веб-сайт на віддаленому сервері](https://dpysmennyi.pythonanywhere.com)

## Технології, задіяні у проекті
* HTML
* CSS
* JS
* Python
* Django
* Bootstrap 5
* SQLite 3
* MySQL
* PythonAnywhere

___

## Структура проекту

У проекті є один застосунок `clinicapp`. У ньому містяться усі веб-сторінки, скріпти, форми та моделі.

### Створення додатку
Щоб створити додаток потрібно ([Документація Django по створенню додатків](https://docs.djangoproject.com/en/5.0/ref/applications/)):
1. Запустити команду `django-admin startapp [ім'я додатка]` в терміналі.
2. Підключити додаток в список `INSTALLED_APPS` у settings.py.

![](https://media.discordapp.net/attachments/759412755937361942/1260182982535286855/image.png?ex=668e645c&is=668d12dc&hm=622b864309a8f90875cd028b230c063afa9bd2aaf4157fe659ee9b2a3afb701a&=&format=webp&quality=lossless&width=780&height=591)

### Створення функції відображення сторінки
Після створення html-файлу main.html, потрібно створити функцію відображення для сторінки.

views.py
```python
from django.shortcuts import render

def main_view(request):
    return render(request, 'clinicapp/main.html')
```

### Підключення функції відображення у urls.py

Підключення функції відображення у файл список urlpatterns, для створення унікального url для веб-сторінки.

urls.py
```python
from django.contrib import admin
from django.urls import path
from clinicapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name="main"),
]
```

### Базовий шаблон base.html

У нашому проєкті застосовуються базові шаблони Django. У файлі base.html прописані лише шапка та підвал сайту, вони є на кожній сторінці. А основна частина (main) та назва сторінки береться з інших html-файлів за допомогою `{% extends '...' %}`

Приклад:

base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    {% block title %}
    {% endblock %}
   ...
</head>
<body>
    <nav>
      ...
    </nav>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>


    <footer>
      ...
    </footer>

</body>
</html>
```
main.html
```
{% extends './base.html' %}
...
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% block title %}
        <title>Головна сторінка</title>
    {% endblock %}
</head>
<body>
   {% block content %}
      ...
   {% endblock %}
   
</body>

```

### Опис файлу views.py

У файлі описані функції відображення кожної сторінки (main, contacts, about, form, services), а також обробка форми після відправлення її користувачем. Після відправки, сервер перевіряє, чи вірно заповнена форма. Якщо ні - повертає помилку, інакше - повідомлення з успіхом та відправка повідомлення з даними користувача на пошту.
___

```python
from django.shortcuts import render, redirect

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
            user = User.objects.create(**form.cleaned_data)
            form = UserForm(request.POST, instance=user)

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

```
Результат відправки повідомлення на e-mail:

![](https://media.discordapp.net/attachments/759412755937361942/1260191643684962355/image.png?ex=668e6c6d&is=668d1aed&hm=1df32436085130d0f480aa843600871d9187b175e17c39ce8e7ff143fdb1b3ca&=&format=webp&quality=lossless&width=769&height=589)

### Опис файлу models.py
Цей файл відповідає за моделі (таблиці) в базі даних. В проєкті міститься лише одна модель User, вона відповідає за збереження даних користувача в базі.

В моделі User 5 полів: name (ім'я), surname (прізвище), e-mail, phone (номер телефону), comment (коментар).

models.py
```python
from django.db import models

# Імпорт модуля для поля з номером телефону
from phonenumber_field.modelfields import PhoneNumberField

# Створення классу моделі User
class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    phone = PhoneNumberField()
    comment = models.TextField()
```

### Ініціалізація бази даних
Щоб ініціалізувати базу даних, потрібно провести міграції. Файли з міграціями вже створені у проекті. Потрібно лише запустити команду `python manage.py migrate` в терміналі. 

Якщо ви будете вносити якісь зміни у файл models.py, перед цим також потрібно створити нові файли міграції за допомогою команди `python manage.py makemigrations`.

### SQLite 3, база даних

**База даних** – сукупність даних, організованих відповідно до концепції, яка описує характеристику цих даних і взаємозв'язки між їх елементами.

У нашому проєкті ми використали базу даних SQLite 3, тому що саме ця база даних дуже гарно підходить для тестування та невеликих навантажень.

![База даних](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/2560px-SQLite370.svg.png)

___

## Підсумок
Проект був зроблений за 1 місяць. Під час роботи дізналися багато чого нового (bootstrap, pythonanywhere, github, робота з хостингом) та закріпили вже відомі знання. Також тепер маємо набагато більше знаннь про сферу психології.

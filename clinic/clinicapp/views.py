from django.shortcuts import render

# Create your views here.

def faq_view(request):
    return render(request, 'clinicapp/faq.html')

def main_view(request):
    return render(request, 'clinicapp/main.html')

def contacts_view(request):
    return render(request, 'clinicapp/contacts.html')

def form_view(request):
    return render(request, 'clinicapp/form.html')

def services_view(request):
    return render(request, 'clinicapp/services.html')

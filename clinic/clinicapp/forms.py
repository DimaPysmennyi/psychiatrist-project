from django import forms
from django.forms import ModelForm
from .models import User
from phonenumber_field.formfields import PhoneNumberField




class UserForm(ModelForm):
    name = forms.CharField(label='', max_length=25)
    surname = forms.CharField(label='', max_length=25)
    phone = PhoneNumberField(label='')
    email = forms.EmailField(label='')
    comment = forms.CharField(label='', widget=forms.Textarea())

    class Meta: 
        model = User
        fields = ["name", "surname", "phone", "email", "comment"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'id': 'name', 'class' : 'input', 'name': 'first-name'})
        self.fields['surname'].widget.attrs.update({'id': 'surname', 'class' : 'input', 'name': 'surname'})
        self.fields['phone'].widget.attrs.update({'id': 'phone', 'class' : 'input', 'name': 'phone'})
        self.fields['email'].widget.attrs.update({'id': 'email', 'class' : 'input', 'name': 'email'})
        self.fields['comment'].widget.attrs.update({'id': 'comment', 'class' : 'textarea', 'name': 'comment'})

        self.fields['name'].widget.attrs.update({'placeholder' : "Ім'я"})
        self.fields['surname'].widget.attrs.update({'placeholder' : "Прізвище"})
        self.fields['phone'].widget.attrs.update({'placeholder' : "Номер телефону"})
        self.fields['email'].widget.attrs.update({'placeholder' : "E-mail"})
        self.fields['comment'].widget.attrs.update({'placeholder' : "Коментар..."})
from django import forms
from django.forms import ModelForm
from django.http import HttpResponse
from .models import User
from django.forms import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from phone_number_validator.validator import PhoneNumberValidator
from validate_email import validate_email

def validate_numbers_in_text(value):
    for char in value:
        if char in "1234567890":
            raise ValidationError(
            ("Ім'я або прізвище не має містити чисел!"),
            params={"value": value},
        )

def validate_one_word(value):
    for char in value:
        if char == " ":
            raise ValidationError(
                ("Введіть своє справжнє прізвище або ім'я!"), params={"value", value}
            )

def validate_email_address(value):
    email = validate_email(value, verify=True)
    if email == False:
        raise ValidationError(
            ("Не дійсний e-mail!"),
            params={"value": value}
        )

def validate_phone_number(value):
    validator = PhoneNumberValidator(api_key='num_live_caNSrTitKZJ7DXgpF3QKFUARdOX95SCHTE9bMFx2')
    if not validator.validate(value):
        raise ValidationError(
            ("")
        )


class UserForm(ModelForm):
    name = forms.CharField(label='', max_length=25)
    surname = forms.CharField(label='', max_length=25)
    phone = PhoneNumberField(label='', validators=[])
    email = forms.EmailField(label='', validators=[validate_email_address])
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
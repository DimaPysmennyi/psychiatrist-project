from django import forms
from django.forms import ModelForm
from .models import User
from django.forms import ValidationError
from django.core.validators import validate_email
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.validators import validate_international_phonenumber

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
    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError(
            ("Не дійсний e-mail!"),
            params={"value": value}
        )


class UserForm(ModelForm):
    name = forms.CharField(label='', max_length=25,validators=[validate_numbers_in_text, validate_one_word])
    surname = forms.CharField(label='', max_length=25, validators=[validate_numbers_in_text, validate_one_word])
    phone = PhoneNumberField(label='', validators=[validate_international_phonenumber])
    email = forms.EmailField(label='', validators=[validate_email_address])
    comment = forms.CharField(label='', widget=forms.Textarea())

    class Meta: 
        model = User
        fields = ["name", "surname", "phone", "email", "comment"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'id': 'name', 'class' : 'input'})
        self.fields['surname'].widget.attrs.update({'id': 'surname', 'class' : 'input'})
        self.fields['phone'].widget.attrs.update({'id': 'phone', 'class' : 'input'})
        self.fields['email'].widget.attrs.update({'id': 'email', 'class' : 'input'})
        self.fields['comment'].widget.attrs.update({'id': 'comment', 'class' : 'input'})

        self.fields['name'].widget.attrs.update({'placeholder' : "Ім'я"})
        self.fields['surname'].widget.attrs.update({'placeholder' : "Прізвище"})
        self.fields['phone'].widget.attrs.update({'placeholder' : "Номер телефону"})
        self.fields['email'].widget.attrs.update({'placeholder' : "E-mail"})
        self.fields['comment'].widget.attrs.update({'placeholder' : "Коментар..."})
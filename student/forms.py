from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    email = forms.EmailField()

    name = forms.CharField(max_length=100)

    phone = forms.CharField(max_length=15)

    course = forms.CharField(max_length=100)


    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'name',
            'phone',
            'course',
            'password1',
            'password2'
        ]
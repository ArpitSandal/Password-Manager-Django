from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username      = forms.CharField(required=False, widget=forms.TextInput(
                    attrs={
                        "placeholder": "Username",
                        "class": "input100"
                        }
                    )
                )
    email      = forms.EmailField(required=False, widget=forms.TextInput(
                    attrs={
                        "placeholder": "Email",
                        "class": "input100"
                        }
                    )
                )
    password1      = forms.CharField(required=False, widget=forms.TextInput(
                    attrs={
                        "placeholder": "Password",
                        "class": "input100",
                         "type": "password",
                        }
                    )
                )
    password2      = forms.CharField(required=False, widget=forms.TextInput(
                attrs={
                    "placeholder": "Confirm Password",
                    "class": "input100",
                    "type": "password",
                    }
                )
            )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    

#For storing login passwords
class LoginStoreForm(forms.ModelForm):
    class Meta:
        model=LoginPass
        fields = [
            'name',
            'username',
        ]



#For storing credit cards
class CreditStoreForm(forms.ModelForm):
    class Meta:
        model = CreditPass
        fields = [
            'name',
            'brand',
            'expirationmonth',
            'expirationyear'
        ]


#For storing secure notes
class NotesStoreForm(forms.ModelForm):
    class Meta:
        model = NotesPass
        fields = [
            'name',
        ]
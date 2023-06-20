from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=60,required=True)
    lastname = forms.CharField(max_length=60,required=True)

    class Meta:
        model = User
        fields = ('username','firstname','lastname','email','password1','password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        if commit:
            user.save()
        return user
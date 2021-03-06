from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group, Permission
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Case
from django.forms import ModelForm


# New User Form 

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=10)

    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

#User Group Form 
class UserGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'permissions': FilteredSelectMultiple("Permission", False, attrs={'rows': '2'}),
        }


class CaseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "name"
    }))
    owner = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "owner"
    }))
    
    workersList = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "workersList"
    }))

    workerGroup = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "WorkerGroup"
    }))

    data = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Data"
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Description"
    }))
    class Meta:
        model = Case
        fields = [
            'name', 'owner', 'workersList', 'workerGroup', 'data', 'description'
        ]

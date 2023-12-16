from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Planner, ToDoList, Reviews
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreatePlanForm(forms.ModelForm):
    class Meta:
        model = Planner
        fields = '__all__'


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'

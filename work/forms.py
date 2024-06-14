from django import forms
from work.models import *

class Register(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        widgets = {
            # 'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            # 'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your password'}),
        }

    
class TaskForm(forms.ModelForm):
    class Meta:
        model=Taskmodel
        fields=['task_name','task_description']
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter a task'}),
            'task_description':forms.Textarea(attrs={'class':'form-control','column':20,'rows':5,'placeholder':'enter a task'})
        }
        
class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))


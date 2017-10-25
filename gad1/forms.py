from django import forms
from gad1.models import Student , Professor , MyModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from tinymce.widgets import TinyMCE

#from .models import Post
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
        
class UploadFileForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class StudentForm(forms.ModelForm):
    student_name = forms.CharField(label='Your name', max_length=20)
    gender = forms.CharField(label='Gender' , max_length=20)
    m_no = forms.CharField(label='Mobile No' , max_length=20)
    year = forms.CharField(label='Year' , max_length=20)
    div = forms.CharField(label='Division' , max_length=20)
    sap = forms.CharField(label='SAP ID' , max_length=20)
    email = forms.CharField(label='Email ID' , max_length=20)
    password = forms.CharField(label='Password' , max_length=20)
    class Meta:
        model = Student
        fields = '__all__'

class StudentLoginForm(forms.Form):
    student_name = forms.CharField(label="Your name", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label='Password' , max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))

class ProfessorForm(forms.ModelForm):
    pro_name = forms.CharField(label='Your name', max_length=20) 
    gender = forms.CharField(label='Gender', max_length=20)
    m_no = forms.CharField(label='Mobile No', max_length=20)
    dept = forms.CharField(label='Department', max_length=20)
    sap = forms.CharField(label='SAP ID', max_length=20)
    email = forms.CharField(label='Email ID', max_length=20)
    password = forms.CharField(label='Password', max_length=20)
    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorLoginForm(forms.Form):
	pro_name = forms.CharField(label='Your name', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'})) 
	password = forms.CharField(label='Password', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))


class MyForm(forms.Form):
    #scontent = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = MyModel
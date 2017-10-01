from django import forms
from gad1.models import Student , Professor , MyModel
#from .models import Post
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
    student_name = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Password' , max_length=20)

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
	pro_name = forms.CharField(label='Your name', max_length=20) 
	password = forms.CharField(label='Password', max_length=20)


class MyForm(forms.Form):
    
    class Meta:
        model = MyModel
from django.shortcuts import get_object_or_404, render ,render_to_response
from gad1.forms import StudentForm,ProfessorForm,StudentLoginForm,ProfessorLoginForm
from gad1.models import FileDb,Professor,Student
from django.core.files import File
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            from django.contrib.auth import authenticate, login
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponseRedirect(reverse('page1'))
    else:
        form = UserCreationForm()
        
    # return render_to_response('registration.html', {
    #     'form': form,
    #     }, context_instance=RequestContext(request))
    return render(request,'registration.html' ,{'form':form})
def page1(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'gad1/page1.html')

def page2(request):
	if request.method == 'POST': # If the form has been submitted...
		#form = ContactForm(request.POST) # A form bound to the POST data
		#if abc01.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			# ...
			pro1= request.POST['profession']
			#print (pro1)
			if pro1=="Teacher":
				form = ProfessorLoginForm()
				return render(request, 'gad1/page24.html',{'form':form})
			else:
				form = StudentLoginForm()
				return render(request, 'gad1/page23.html',{'form':form})

def page3(request):
	# if request.method == 'POST':
	# 	form  = StudentForm(request.POST)
	# 	if form.is_valid:
	# 		obj = Student()
	# 		obj.name = form.cleaned_data['student_name']
	# 		obj.save()
			form = StudentForm()
			return render(request, 'gad1/page3.html',{'form':form})

def page4(request):
	form=ProfessorForm()
	return render(request,'gad1/page4.html',{'form':form})

#def page23(request):
#	return render(request, 'gad1/page23.html')

def page6(request):
	if request.POST :
		form = ProfessorForm(request.POST)
		if form.is_valid():
			prof = form.save()
	return render(request, 'gad1/page6.html')

def page61(request):
	if request.method == 'POST':
		form = ProfessorLoginForm(request.POST)
		if form.is_valid():
			#user = form.save()
			# from django.contrib.auth import authenticate, login
			# user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
			# login(request, user)
			try:
				
				a1 = Professor.objects.get(pro_name=form.cleaned_data.get('pro_name'),password=form.cleaned_data.get('password'))
				#print(a)
				if  not a1:
					return HttpResponseRedirect(reverse('page1'))
				return render(request, 'gad1/page6.html')
			except Professor.DoesNotExist:
				return HttpResponseRedirect(reverse('page1'))##
		else:
			form = UserCreationForm()
			return render(request, 'gad1/page1.html')


def page51(request):
	if request.method == 'POST':
		form = StudentLoginForm(request.POST)
		if form.is_valid():
			#user = form.save()
			# from django.contrib.auth import authenticate, login
			# user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
			# login(request, user)
			try:
				
				a2 = Student.objects.get(student_name=form.cleaned_data.get('student_name'),password=form.cleaned_data.get('password'))
				#print(a)
				if  not a2:
					return HttpResponseRedirect(reverse('page1'))
				return render(request, 'gad1/page5.html')
			except Student.DoesNotExist:
				return HttpResponseRedirect(reverse('page1'))##
		else:
			form = UserCreationForm()
			return render(request, 'gad1/page1.html')

def page5(request):
	if request.POST :
		form = StudentForm(request.POST)
		if form.is_valid():
			student = form.save()
	return render(request, 'gad1/page5.html')

def page7(request):
	file = FileDb.objects.get()
	filename = file.source.read()
	#save edited file:
	if request.method == "POST":
		from django.core.files import File
		f = open(file.source.path, 'w')
		content = request.POST['content']
		f.write(content)
		f = File(f)
		file.source = f
		file.save()
	return render_to_response('page7.html',{'file':file,'filename':filename},context_instance=RequestContext(request))


def index(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'gad1/page1.html')

def page8(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'gad1/page8.html')

def page9(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'gad1/page9.html')

def yp(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'gad1/page1.html')
#def login1(request):
   # question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'registration/login.html')


def page10(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'gad1/page10.html')

def updatefile(request):
    #file = UploadedFile.objects.get(pk=id)
    if request.method == "POST":
       #from django.core.files import File
       #f = open(file.docfile.path,'w+b')
       import time
       timestr = time.strftime("%Y%m%d-%H%M%S")
       #timest = 'C:\\Users\Gargee Bhase\pana\\' + timestr
       timest = 'C:\\Users\Gargee Bhase\pana\\abcd'

       fi=open(timest,'w+')
       f = File(fi)
       content = request.POST['text1']
       #abcde = tinymce.dom.getContent({format : 'text'});
       f.write(content)
       #file.docfile = File(f)
       #file.save()
       #return HttpResponseRedirect('/home/')
       #abcde = selection.getContent({format : 'text'});
       return render(request, 'gad1/page6.html')

    else:
       docfile = file.docfile.read()

       return render_to_response('gad1/updatefile.html',{'file':file,  'docfile' :
                   docfile}, context_instance=RequestContext(request))

def updatefile2(request):
	if request.method == "POST":
		if request.POST.get('numero', False):
			m = request.POST['numero']
			import time
			timestr = time.strftime("%Y%m%d-%H%M%S")
			#timest = 'C:\\Users\Gargee Bhase\pana\\' + timestr
			timest = 'C:\\Users\Gargee Bhase\pana\\' + m
			fi=open(timest,'w+')
			f = File(fi)
			content = request.POST['text1']
			f.write(content)
			return render(request, 'gad1/page5.html')

	else:
		docfile = file.docfile.read()

		return render_to_response('gad1/updatefile.html',{'file':file,  'docfile' :
		                   docfile}, context_instance=RequestContext(request))

def page18(request):
	du = open('C:\\Users\Gargee Bhase\pana\\abcd','r')
	o = File(du)
	context = {}
	context["uploadedFile"]=o.read()
	return render_to_response('gad1/page18.html',context)

def page19(request):
	#if request.method == 'POST':
		#if request.POST.get('magic', False):
			#m = request.POST['magic']
			your_parameter = request.GET['parameter']
			durr = 'C:\\Users\Gargee Bhase\pana\\' + your_parameter
			du = open(durr,'r')
			o = File(du)
			context = {}
			context["uploadedFile"]=o.read()
			if context == {}:
				context ="Assignment not submitted"
			return render_to_response('gad1/page19.html',context)

def pagechat(request):
	return render(request, 'gad1/pagechat.html')

def teach2(request):
	return render(request, 'gad1/teach2.html')
# def pagechat(request):
# 	chatbot = ChatBot("Ron Obvious")
# 	conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome."
# ]

# chatbot.set_trainer(ListTrainer)
# chatbot.train(conversation)
# response = chatbot.get_response("Good morning!")
# print(response)


#, id

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

# def handle_uploaded_file(f):
#     with open('C:/gargee_june/form1a.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)



#updatefile2
#file = UploadedFile.objects.get(pk=id)
#from django.core.files import File
       #f = open(file.docfile.path,'w+b')
       #abcde = tinymce.dom.getContent({format : 'text'});


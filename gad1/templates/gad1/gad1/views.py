from django.shortcuts import get_object_or_404, render ,render_to_response
from gad1.forms import StudentForm,ProfessorForm,StudentLoginForm,ProfessorLoginForm
from gad1.models import FileDb
from django.core.files import File
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

# def page23(request):
# 	return render(request, 'gad1/page5.html')

def page5(request):
	if request.POST :
		form = ProfessorForm(request.POST)
		if form.is_valid():
			prof = form.save()
	return render(request, 'gad1/page5.html')

def page6(request):
	if request.POST :
		form = StudentForm(request.POST)
		if form.is_valid():
			prof = form.save()
	return render(request, 'gad1/page6.html')

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
       timest = 'C:\\Users\Gargee Bhase\pana\\' + timestr
       fi=open(timest,'w+')
       f = File(fi)
       content = request.POST['text1']
       f.write(content)
       #file.docfile = File(f)
       #file.save()
       #return HttpResponseRedirect('/home/')
       return render(request, 'gad1/page10.html')

    else:
       docfile = file.docfile.read()

       return render_to_response('gad1/updatefile.html',{'file':file,  'docfile' :
                   docfile}, context_instance=RequestContext(request))


def page18(request):
	du = open('C:\\Users\Gargee Bhase\pana\\bc','r')
	o = File(du)
	context = {}
	context["uploadedFile"]=o.read()
	return render_to_response('gad1/page18.html',context)

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
from django.shortcuts import get_object_or_404, render


def page1(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'gad1/page1.html')

def index(request):
   # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'gad1/page1.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('C:/gargee_june/form1a.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
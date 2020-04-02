from django.shortcuts import render
from .forms import ClientsFileForm
from .models import ClientsFile


def home(request):
    files = ClientsFile.objects.all()
    return render(request, 'upload/home.html', {'files': files})


def upload(request):
    if request.method == 'POST':
        form = ClientsFileForm(request.POST, request.FILES)
        print("upload request files: " + str(request.FILES['document']))
        if form.is_valid():
            form.save()
            message = "File " + str(request.FILES['document']) + " was uploaded successfully!"

            form = ClientsFileForm()
            return render(request, 'upload/upload.html', { 'form': form, 'message': message })
    else:
        form = ClientsFileForm()
        return render(request, 'upload/upload.html', { 'form': form })

from django.shortcuts import render
from django.http import HttpResponse
from .models import  FilesUplaod
# Create your views here.
def fileUpload(request):
    if request.method == "POST":
        uploadedFile = request.FILES["file"]
        document = FilesUplaod.objects.create(file=uploadedFile)
        document.save()
        return HttpResponse("File uploaded successfully!")
    return render(request, "fileUpload.html", {'nam': 'Ravi'})
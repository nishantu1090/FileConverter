import os.path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  FilesUplaod
from FileConverter import  settings
# Create your views here.
def uploadFile(request):
    if request.method == "POST":
        uploadedFile = request.FILES["file"]
        document = FilesUplaod.objects.create(file=uploadedFile)
        document.save()
        return redirect(downloadFile)
    return render(request, "fileUpload.html")

def downloadFile(request):
    context = {'files': FilesUplaod.objects.all()}
    return render(request, 'download.html', context)
    if request.method == "POST":
        file_path = os.path.join(settings.MEDIA_ROOT)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    return render(request, "download.html")
import os.path
from os import walk
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FilesUplaod
from FileConverter import settings
from django.core.files.base import ContentFile
# Create your views here.
def uploadFile(request):
    if request.method == "POST":
        uploadedFile = request.FILES["file"]
        document = FilesUplaod.objects.create(file=uploadedFile)
        document.save()
        file_path = os.path.join(settings.MEDIA_ROOT)
        os.system('audio-to-midi '+settings.MEDIA_ROOT+'/'+document.filename()+' -b 120 -t 30')
        #os.system('rm '+settings.MEDIA_ROOT+'/'+document.filename())
        os.system('mv ./'+document.filename()+'.mid '+file_path)
        file_path = os.path.join(settings.MEDIA_ROOT)
        with open(file_path +'/'+document.filename()+'.mid', 'rb') as fh:
            content = ContentFile(fh.read(), name="./"+document.filename()+'.mid')
            document = FilesUplaod.objects.create(file=content)
            document.save()
            fh.close()
        return redirect(downloadFile)
    return render(request, "fileUpload.html")

def downloadFile(request):
    context = {'files': FilesUplaod.objects.all()}
    return render(request, 'download.html', context)
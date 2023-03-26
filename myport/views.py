from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.http import FileResponse
from django.conf import settings
from django.contrib import auth,messages
from django.contrib.auth.models import User
import os
from .models import *
from django.core.validators import validate_email



def port(request):
    if(request.method=="POST"):
        c = Contact()
        c.name = request.POST.get('name')
        c.email = request.POST.get('email')
        c.subject = request.POST.get('subject')
        c.message = request.POST.get('message')
        c.save()
        messages.success(request,"Message Sent!!!")
    return render(request,"port.html")




def download_resume(request):
    # Get the resume file path
    resume_path = os.path.join(settings.BASE_DIR, 'static', 'Gaurav-Saini.pdf')

    # Open the file in read-only mode
    resume_file = open(resume_path, 'rb')

    # Create a FileResponse object to represent the file
    response = FileResponse(resume_file)

    # Set the Content-Disposition header to force browser to download file
    response['Content-Disposition'] = 'attachment; filename="Gaurav-Saini.pdf"'

    return response




    

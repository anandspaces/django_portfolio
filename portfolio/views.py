from django.shortcuts import render
from .forms import AudienceForm # new
from django.http import FileResponse,HttpResponse,HttpResponseNotFound #new
from django.conf import settings # new
import os
import mimetypes

def index(request):
    form = AudienceForm()
    if request.method == 'POST':
        form = AudienceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'index.html',context)

def download_resume(request):
    # Path to the resume PDF file
    resume_path = os.path.join(settings.STATIC_ROOT, 'files', 'resume.pdf')
    
    # Open the file and return it as a FileResponse
    return FileResponse(open(resume_path, 'rb'), as_attachment=True, filename='resume.pdf')

def download_file(request):
    # Fill these variables with real values
    fl_path = 'static/files/resume.pdf'  # Adjust the path to match the actual location of your resume PDF file
    filename = 'resume.pdf'

    if os.path.exists(fl_path):
        with open(fl_path, 'rb') as fl:
            mime_type, _ = mimetypes.guess_type(fl_path)
            response = HttpResponse(fl, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
    else:
        return HttpResponseNotFound("File not found")
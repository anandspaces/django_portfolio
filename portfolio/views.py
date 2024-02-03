from django.shortcuts import render
# from django.views.generic import TemplateView # new
from .forms import AudienceForm # new

# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'index.html'

def index(request):
    form = AudienceForm()
    if request.method == 'POST':
        form = AudienceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'index.html',context)
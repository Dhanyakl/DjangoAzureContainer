from django.shortcuts import render,redirect
from .forms import FileUploadForm



# Create your views here.

def index(request):
    if request.method== 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
          
            upload.save()
            return redirect('/')
        else:
             context= {'form': FileUploadForm() }
             return render(request,'index.html',context)

    context= {'form': FileUploadForm() }
    return render(request,'index.html',context)
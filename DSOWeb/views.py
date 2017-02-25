from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UploadFileForm

from .dso import save_file_calib


# Create your views here.
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            res = save_file_calib(request.FILES["file"], form.cleaned_data["title"], form.cleaned_data['user'], form.cleaned_data['phone'], form.cleaned_data['calibB'])
            return HttpResponseRedirect("/DSOWeb/"+res)

    else:
        form = UploadFileForm()

    return render(request, 'DSOWeb/upload.html', {'form': form})


def calibexist(request):
    return render(request,'DSOWeb/calibexist.html')

def calibcreated(request):
    return render(request,'DSOWeb/calibcreated.html')

def caliberror(request):
    return render(request,'DSOWeb/caliberror.html')

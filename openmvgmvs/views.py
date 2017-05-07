import os

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import UploadFile

from .openmvgmvs import save_file


# Create your views here.
def upload_file(request):
    if request.method == "POST":
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            res = save_file(request.FILES["file"], form.cleaned_data["title"], form.cleaned_data['user'])
            #return HttpResponseRedirect("/3DReconstruct/"+res)

            if os.path.exists(res):
                with open(res, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/zip")
                    response['Content-Disposition'] = 'inline; filename=3D_res.zip'
                    return response
            else:
                return "result"

    else:
        form = UploadFile()

    return render(request, '3DReconstruct/upload.html', {'form': form})


def calibexist(request):
    return render(request,'DSOWeb/calibexist.html')

def result(request):
    return render(request,'3DReconstruct/OBJViwer.html')

def calibcreated(request):
    return render(request,'DSOWeb/calibcreated.html')

def caliberror(request):
    return render(request,'DSOWeb/caliberror.html')


def model3dcreated(request):
    return render(request,'DSOWeb/model3dcreated.html')


def calibdontexist(request):
    return render(request,'DSOWeb/calibdontexist.html')
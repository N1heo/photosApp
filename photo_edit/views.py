from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from photo_edit.models import Photo_edit


# Create your views here.
def say_hello(request):
    if request.method == 'POST':
        imgmdl = Photo_edit()
        img = request.FILES.get('img')
        imgmdl.imagename = 'sample1'
        imgmdl.image = img
        imgmdl.save()
    obj = Photo_edit.objects.last()
    context = {
        'obj':obj,
    }
    return render(request, "photoedit.html", context)
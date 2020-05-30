from django.shortcuts import render
from django.http import HttpResponse


#  Create your views here.
def index(request):
    from django.conf import settings
    print(settings.BASE_DIR)  # MY_PATH/proy_gestor/proy_gestor

    return HttpResponse("Bienvenidos al app core")

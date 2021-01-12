from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
from .models import *
import json
from django.http import JsonResponse
from django.core import serializers
from Client.models import *
from .form import *
from django.http import FileResponse
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from random import randrange

import os
from datetime import datetime , date    
# from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.deprecation import MiddlewareMixin



# Create your views here.
class Index(View):
    def get(self,request):
        authors=Add.objects.all().order_by('-id')
        contex = {'authors':authors}
        qs_json = serializers.serialize('json', authors)
        return HttpResponse(qs_json, content_type='application/json')


class Download(View):
    def get(self,request, url):
        dbUrl=SecretUrl.objects.get(url_hash=url)
        
      
        if dbUrl.expires < datetime.now():
            return HttpResponse(dbUrl.expires)
        # url = get_object_or_404(SecretUrl, url_hash=hash, expires__gte=datetime.now())
        path='Composer-Setup.exe'
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/file")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        raise Http404


class AddClient(View):
    def get(self,request):
        return HttpResponse('aa')
    def post(self,request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            url=randrange(10000, 10000000000, 5)
            SecretUrl.objects.create(url_hash=url, expires='2021-01-11 11:19:19')
            path='Composer-Setup.exe'
            file_path = os.path.join(settings.MEDIA_ROOT, path)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/file")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
            raise Http404
        return HttpResponse('Thanks')

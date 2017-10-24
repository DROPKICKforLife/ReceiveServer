from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from app.models import Receive
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

@csrf_exempt
def test(request):
    post_data = urlencode({"send":"hi"})
    req = Request("http://127.0.0.1:8000/app/",data=post_data.encode('utf-8'))
    response = urlopen(req)
    result = response.read().decode('utf-8')
    return HttpResponse(result)
@csrf_exempt
def func(request):
    if request.method == "POST":

        print(request.POST['send'])
        Receive(rec_text=request.POST['send'],rec_date=timezone.now()).save()
        lists= Receive.objects.all()
        txt = ""
        for i in lists:
            txt += str(i.id) + " : " + i.rec_text + " - " +str(i.rec_date) + "\n"
        print(txt)
        context = {'lists' : txt}
        return HttpResponse(context['lists'])
    else:
        print("GET")
        return HttpResponse("hello")
    pass
# Create your views here.

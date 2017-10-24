from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from app.models import Receive
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from konlpy.tag import Twitter

def twitter(msg):
    t = Twitter()
    print("초기화")
    data = t.pos(msg,norm=True,stem=True)
    return data
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
        inputData = request.POST['send']
        print(inputData)
        try:
            kon = twitter(inputData)
        except:
            print("오류")
        else:
            print(kon)
        Receive(rec_text=inputData,rec_date=timezone.now(),rec_konlpy=kon).save()
        lists= Receive.objects.all()
        txt = ""
        for i in lists:
            txt += str(i.id) + " : " + i.rec_text + " - " +str(i.rec_date)+" // " +str(i.rec_konlpy)+ "\n"
        print(txt)
        context = {'lists' : txt}
        return HttpResponse(context['lists'])
    else:
        print("GET")
        return HttpResponse("hello")
    pass
# Create your views here.

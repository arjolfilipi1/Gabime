from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView
from .models import Gab,Per,Op
from django.db.models import Count

from django.views.decorators.csrf import csrf_exempt
def index(request):
    all = Gab.objects.all()
    

    return HttpResponse("Hello, world. You're at the polls index.")
@csrf_exempt
def Gjej(request):
    print('gjej')
    Last = Gab.objects.order_by('-id')[:5]
    se= Per.objects.get(cir=slug)
    print(se)
    context = {
        'Last':Last,
        'slug':slug
    }
    return render(request, 'info.html', context)
@csrf_exempt    
def Regis(request,*args):
    oid = request.GET.get("id")
    test = (Op.objects.filter(num=oid).exists())
    if oid=='':
        if test:
            return render(request, 'log.html',context={'e':test})
        else:
            return render(request, 'log.html',context={'e':test})
    elif test:
        op = Op.objects.get(num=oid)
        
        Last = Gab.objects.order_by('-id')[:5]
        context = {
            'Last':Last,'id':oid
                }
        slug = (request.GET.get(""))
        if request.method == 'GET':
            d = (request.GET.get("flexRadioDefault"))         
            slug = (request.GET.get("cir"))
            context = {'Last':Last,'slug':slug,'id':oid}
        
            if slug:
                try:
                    se= Per.objects.get(cir=slug)
                    if d:
                        Gab.objects.create(cir=slug,grup=se.grup,pos=d)
                        Last = Gab.objects.order_by('-id')[:5]
                        context = {'Last':Last,'id':oid}
                        return render(request, 'info.html', context)
                except:
                    se= False
                if se:
                    context = {'slug':slug,'Last':Last,'start':se.start,"end":se.end,'id':oid
                        }
                else:
                    context = {
                'slug':slug,'Last':Last,'id':oid
                }
        
        return render(request, 'info.html', context)
    else:
        print("here")
        return render(request, 'log.html',context={'e':True})


def FormView(request):
    Last = Gab.objects.all()
    #[:5]
    
    context = {
        'Last':Last,
    }
    print(context)

    return render(request, 'info.html', context)

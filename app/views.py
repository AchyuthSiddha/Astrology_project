from django.shortcuts import render
import datetime
import random
# Create your views here.


def Astro(request):
    time=datetime.datetime.now()
    h=int(time.strftime('%H'))
    name_list=['NTR','PK','Bhalaya','ramacharan','AA','ram','nithin','mohanlal']
    msg_list=['Golden days are head',
              'better to sleep more time even in class room also...',
              'Tomorrow will be the best day of your life',
              'Tomorrow is the perfect day to propose ur GF',
              'very soon you will get job']
    if h<12:
        s='Good morning'
    elif h<16:
        s='Good afternoon'
    elif h<21:
        s='Good evening'
    else:
        s='Good night'
    names=random.choice(name_list)
    message=random.choice(msg_list)
    d={'names':names,'msg':message,'date':time,'day':s}

    return render(request,'astro.html',d)
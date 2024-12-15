from lib2to3.fixes.fix_input import context

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from main.models import *


def home_view(request):
    return render(request,'home.html')

def bino_view(request):
    if request.method=='POST':
        Bino.objects.create(
            bino_nom=request.POST.get('bino'),
            asosiy=request.POST.get('asosiy'),
        )
        return redirect('bino')

    binolar=Bino.objects.all()
    q_soz = request.GET.get('q_soz')
    if q_soz is not None:
        binolar = binolar.filter(bino_nom__contains=q_soz)
    context={
        'binolar':binolar,
        'q_soz':q_soz
    }
    return render(request,'bino_nomlari.html',context)
def fakultet_view(request):
    fakultetlar=Fakultet.objects.all()
    q_soz=request.GET.get('q_soz')
    if q_soz is not None:
        fakultetlar=fakultetlar.filter(fakultet_nomi__contains=q_soz)

    context={
        'fakultetlar':fakultetlar,
        'q_soz':q_soz
    }
    return render(request,'fakultetlar.html',context)

def yonalishlar_view(request):
    if request.method=='POST':
        Yonalish.objects.create(
            yonalish_nomi=request.POST.get('yonalish'),
            guruh_soni=request.POST.get('guruh'),
            talaba_soni=request.POST.get('talaba'),
            titur_soni=request.POST.get('titur'),
        )
        return redirect('yonalish')
    yonalishlar=Yonalish.objects.all()
    q_soz=request.GET.get('q_soz')
    if q_soz is not None:
        yonalishlar=yonalishlar.filter(yonalish_nomi__contains=q_soz)
    context={
        'yonalishlar':yonalishlar,
        'q_soz':q_soz
    }
    return render(request,'Yonalishlar.html',context)
def kafedra_view(request):
    kafedralar=Kafedra.objects.all()
    q_soz=request.GET.get('q_soz')
    if q_soz is not None:
        kafedralar=kafedralar.filter(kafedra_nomi__contains=q_soz)
    context={
        'kafedralar':kafedralar,
        'q_soz':q_soz
    }
    return render(request,'kafedralar.html',context)
def kafedra_mudiri_view(request):
    if request.method=='POST':
        Kafedra_mudiri.objects.create(
            ism=request.POST.get('ism'),
            familya=request.POST.get('familya'),
            yosh=request.POST.get('yosh'),
            telefon_raqam=request.POST.get('telefon_raqam'),
            jinsi=request.POST.get('jinsi'),
             )
        return redirect('kafedra_mudiri')

    mudirlar=Kafedra_mudiri.objects.all()
    q_soz = request.GET.get('q_soz')
    if q_soz is not None:
        mudirlar=mudirlar.filter(ism__contains=q_soz)
    context={
        'mudirlar':mudirlar,
        'q_soz':q_soz

    }
    return render(request,'kafedra_mudiri.html',context)
def ustoz_view(request):
    ustozlar=Ustoz.objects.all()
    q_soz = request.GET.get('q_soz')
    if q_soz is not None:
        ustozlar=ustozlar.filter(ism__contains=q_soz)
    context={
        'ustozlar':ustozlar,
        'q_soz': q_soz
    }
    return render(request,'ustozlar.html',context)
def talaba_view(request):
    talabalar = Talaba.objects.all()
    q_soz=request.GET.get('q_soz')
    if q_soz is not None:
        talabalar=talabalar.filter(ism__contains=q_soz)
    context={
        'talabalar':talabalar,
        'q_soz':q_soz
    }
    return render(request,'talabalar.html',context)
def titur_view(request):
    if request.method=='POST':
        Titur.objects.create(
            ism=request.POST.get('ism'),
            familya=request.POST.get('familya'),
            yosh=request.POST.get('yosh'),
            telefon_raqam=request.POST.get('telefon_raqam'),
            jinsi=request.POST.get('jinsi')

        )
        return redirect('titurlar')
    titurlar=Titur.objects.all()
    q_soz = request.GET.get('q_soz')
    if q_soz is not None:
        titurlar=titurlar.filter(ism__contains=q_soz)
    context={
        'titurlar':titurlar,
        'q_soz': q_soz
    }
    return render(request,'titurlar.html',context)
def guruh_view(request):
    guruhlar=Guruh.objects.all()
    q_soz = request.GET.get('q_soz')
    if q_soz is not None:
        guruhlar=guruhlar.filter(guruh_nomi__contains=q_soz)
    context={
        'guruhlar':guruhlar,
        'q_soz':q_soz
    }
    return render(request,'guruhlar.html',context)
def talaba_index_view(request,talaba_id):
    talaba=Talaba.objects.get(id=talaba_id)
    context={
        'talaba':talaba
    }
    return render(request,'talaba_index.html',context)
def bino_index_view(request,bino_id):
    bino=Bino.objects.get(id=bino_id)
    context={
        'bino':bino
    }
    return render(request,'bino_index.html',context)
def fakultet_index_view(request,fakultet_id):
    fakultet=Fakultet.objects.get(id=fakultet_id)
    context={
        'fakultet':fakultet
    }
    return render(request,'fakultet_index.html',context)
def kafedra_index_view(request,kafedra_id):
    kafedra=Kafedra.objects.get(id=kafedra_id)
    context={
        'kafedra':kafedra
    }
    return render(request,'kafedra_index.html',context)
def kafedra_mudiri_index_view(request,kafedra_mudiri_id):
    kafedra_mudiri=Kafedra_mudiri.objects.get(id=kafedra_mudiri_id)
    context={
        'kafedra_mudiri':kafedra_mudiri
    }
    return render(request,'kafedra_mudiri_index.html',context)
def ustoz_index_view(request,ustoz_id):
    ustoz=Ustoz.objects.get(id=ustoz_id)
    context={
        'ustoz':ustoz
    }
    return render(request,'ustoz_index.html',context)
def titur_index_view(request,titur_id):
    titur=Titur.objects.get(id=titur_id)
    context={
        'titur':titur
    }
    return render(request,'titur_index.html',context)
def guruh_index_view(request,guruh_id):
    guruh=Guruh.objects.get(id=guruh_id)
    context={
        'guruh':guruh
    }
    return render(request,'guruh_index.html',context)
def yonalish_index_view(request,yonalish_id):
    yonalish=Yonalish.objects.get(id=yonalish_id)
    context={
        'yonalish':yonalish
    }
    return render(request,'yonalish_index.html',context)
def talaba_delete_view(request,talaba_id):
    talaba=get_object_or_404(Talaba,id=talaba_id)
    talaba.delete()
    return redirect('talabalar')
def bino_delete_view(request,bino_id):
    bino=get_object_or_404(Bino,id=bino_id)
    bino.delete()
    return redirect('bino')
def fakultet_delete_view(request,fakultet_id):
    fakultet=get_object_or_404(Fakultet,id=fakultet_id)
    fakultet.delete()
    return redirect('fakultet')
def yonalish_delete_view(request,yonalish_id):
    yonalish=get_object_or_404(Yonalish,id=yonalish_id)
    yonalish.delete()
    return redirect('yonalish')
def kafedra_delete_view(request,kafedra_id):
    kafedra=get_object_or_404(Kafedra,id=kafedra_id)
    kafedra.delete()
    return redirect('kafedra')
def kafedra_mudiri_delete_view(request,kafedra_mudiri_id):
    kafedra_mudiri=get_object_or_404(Kafedra_mudiri,id=kafedra_mudiri_id)
    kafedra_mudiri.delete()
    return redirect('kafedra_mudiri')
def ustoz_delete_view(request,ustoz_id):
    ustoz=get_object_or_404(Ustoz,id=ustoz_id)
    ustoz.delete()
    return redirect('ustozlar')
def titur_delete_view(request,titur_id):
    titur=get_object_or_404(Titur,id=titur_id)
    titur.delete()
    return redirect('titurlar')
def guruh_delete_view(request,guruh_id):
    guruh=get_object_or_404(Guruh,id=guruh_id)
    guruh.delete()
    return redirect('guruhlar')
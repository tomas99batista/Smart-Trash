from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from . import sensor
# Create your views here.

def index(request):
    bins_list = Bin.objects.all()

    context = {'bins_list' : bins_list,}

    return render(request, 'index.html', context=context)


def bin_by_id(request, id):
    bin_details = Regist.objects.filter(trash_bin__bin_id=id).order_by('-id_regist')
    trash_bin = Bin.objects.get(bin_id=id)
    try:
        bin_status = Regist.objects.filter(trash_bin__bin_id=id).latest('id_regist').occupation_value
    except Exception as e:
        bin_status = None
        print(e)
    
    context = {'bin_details' : bin_details,
                'bin': trash_bin,
                'bin_status':bin_status}

    return render(request, 'bin_details.html', context=context)

def update_bin(request):
    # Aqui vai o raspy trabalhar boyyyyyy
    bin_id = request.POST.get("bin_id", "")
    try:
        occupation_value = sensor.get_value_distance(3)
        trash_bin = Bin.objects.get(bin_id=bin_id)
        return redirect("bin_detail", id=bin_id)
    except Exception as e:
        return HttpResponse('<h1>Sensor not connected!</h1>')

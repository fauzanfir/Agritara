import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from add_item.models import BarangPetani

# from petani_home.models import BarangPetani

def index(request):
    return render(request, 'index.html')
 
def show_as_json(request):
    list_barang = BarangPetani.objects.all()

    # barang_filtered = list_barang.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", list_barang), content_type="application/json")

def show_barang_petani(request):
    list_barang = BarangPetani.objects.all()
    # barang_filtered = list_barang.filter(user=request.user)
    context = {
        'list_barang': list_barang
    }
    return render(request, 'homepetani.html', context)

def get_data_json_from_tambah(request):
    list_barang = BarangPetani.objects.all()

    # barang_filtered = list_barang.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", list_barang), content_type="application/json")


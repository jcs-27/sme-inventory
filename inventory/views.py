from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("SME Inventory System is live!")
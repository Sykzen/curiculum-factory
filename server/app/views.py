from django.shortcuts import render,redirect,reverse


def index(request):
    return render(request, 'index.html')
def espace_recruteur(request):
    return render(request,'espace_recruteur.html')
def applicant(request):
    return render(request,'applicant.html')
def mon_espace(request):
    return render(request,'mon_espace.html')
    

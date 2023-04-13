from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Hai(request):
    if request.method=='POST':
        name=request.POST['Un']
        Password=request.POST['Pw']
        print('name')
        print('Pw')
        return HttpResponse('Request Accepted')

    return render(request,'Hai.html')
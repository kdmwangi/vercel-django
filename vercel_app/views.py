from django.shortcuts import render

# Create your views here.

def Index(request):

    return render(request,'vercel_app/index.html')

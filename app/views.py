from django.shortcuts import render

# Create your views here.
def bs_cdn(request):
    return render(request,'bs_cdn.html')

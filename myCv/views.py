from django.shortcuts import render

# Create your views here.
def cv(request):
    return render(request,"show.html")
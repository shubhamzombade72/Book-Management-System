from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def indexpage(request):
    return render(request, "index.html")  
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def show_home(request):
    return render(request, 'home/home.html')

def show_about(request):
    return render(request, 'home/about.html')
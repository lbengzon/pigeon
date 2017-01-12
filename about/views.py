from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def show_about(request):
    return render(request, 'about/about.html')
    #return render_to_response('about/about.html')
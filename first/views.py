from django.shortcuts import render


# Create your views here.
def base_html(request):
    return render(request, 'base.html')

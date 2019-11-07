from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from first.forms import SignUpForm


# Create your views here.
def base_html(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_pass)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

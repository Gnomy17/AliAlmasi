from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from first.forms import SignUpForm, LoginForm, ContactForm


# Create your views here.
def base_html(request):
    return render(request, 'base.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        raw_username = request.POST['username']
        userFoundError = None
        pass_mismatch = None
        if User.objects.filter(username__exact=raw_username):
            userFoundError = True
        if request.POST['password1'] != request.POST['password2']:
            pass_mismatch = True
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_pass)
            auth_login(request, user)
        return render(request, 'register.html',
                      {'form': form, 'userFoundError': userFoundError,
                       'pass_mismatch': pass_mismatch})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('/')
        else:
            error = "You suck!"
            form = LoginForm()
            # return redirect('/login', {'error': error})
            return render(request, 'login.html', {'error': error, 'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send_mail(
            #     request.POST['title'],
            #     request.POST['text'],
            #     request.POST['email'],
            #     # 'webe19lopers@gmail.com'
            #     ['ahmadrahimiuni@gmail.com',]
            # )
            email = EmailMessage(request.POST['title'], request.POST['text'], to=['webe19lopers@gmail.com'])
            # email.send(fail_silently=False)
            return redirect('/contact_success')
        else:
            print("BAaaaaaaaaaaaa! no success!")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')

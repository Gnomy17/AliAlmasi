from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from first.forms import SignUpForm, LoginForm, ContactForm, ChangeInfo, CourseForm

# Create your views here.
from first.models import Course


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
            email = EmailMessage(request.POST['title'], request.POST['text'] + request.POST['email'],
                                 to=['webe19lopers@gmail.com'])
            # email.send(fail_silently=False)
            return redirect('/contact_success')
        else:
            print("BAaaaaaaaaaaaa! no success!")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')


@login_required
def profile(request):
    return render(request, 'profile.html',
                  {'user': request.user, 'imgpath': "/media/" + request.user.username + '.png'})


@login_required
def change_info(request):
    if request.method == 'POST':
        form = ChangeInfo(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            file = request.FILES.get('filee')
            dest = open('media/' + user.username + '.png', 'wb+')
            for chunk in file.chunks():
                dest.write(chunk)
            if form.cleaned_data.get('first_name'):
                user.first_name = form.cleaned_data.get('first_name')
                print("first name changed")
            if form.cleaned_data.get('last_name'):
                user.last_name = form.cleaned_data.get('last_name')
                print("last name changed")
            user.save()
            return redirect('/profile')
        else:
            for msg in form.errors:
                print(msg)
    else:
        form = ChangeInfo()
    return render(request, 'change_info.html', {'form': form})


def panel(request):
    return render(request, 'panel.html')


def new_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/panel')
    else:
        form = CourseForm()
    return render(request, 'new_course.html', {'form': form})


def courses(request):
    return render(request, 'courses.html', {'courses': Course.objects.all()})

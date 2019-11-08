"""Webeloped URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from first.views import base_html, register, login, logout, contact_us, contact_success, profile, change_info, \
    new_course, courses
from first.views import base_html, register, login, logout, contact_us, contact_success, panel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_html, name='home'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('contact', contact_us, name='contact'),
    path('panel', panel, name='panel'),
    path('contact_success', contact_success, name='contact_success'),
    path('profile', profile, name='profile'),
    path('change_info', change_info, name='change_info'),
    path('new_course', new_course, name='new_course'),
    path('courses', courses, name='courses'),
]

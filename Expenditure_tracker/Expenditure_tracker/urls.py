"""Expenditure_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views


#Projects URLS file
#Contains URLS for admin,index,thankyou,about,login pages
#also contain link for applications URLs file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Exp_trac_app.urls',namespace='expenditures')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('index',views.HomePage.as_view(),name='home'),
    path('thanks',views.ThanksPage.as_view(),name='thanks'),
    path('about',views.AboutPage.as_view(),name='about'),
    path('',auth_views.LoginView.as_view(template_name='Exp_trac_app/login.html', redirect_authenticated_user=True),name='login'),


]

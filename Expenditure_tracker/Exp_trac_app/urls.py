from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name='Exp_trac_app'

#applications URLS file
#Contains URLS for signup,logout,addition of expense page, editing of expense page
#and For view the expenses page.

urlpatterns=[
path('logout/',auth_views.LogoutView.as_view(),name='logout'),
path('signup/',views.SignUp.as_view(),name='signup'),
path('addexp/',views.AddExp.as_view(),name='addexp'),
path('editexp/',views.EditExp.as_view(),name='editexp'),
path('viewexp/',views.ViewExp.as_view(),name='viewexp'),
]

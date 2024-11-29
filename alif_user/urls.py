from django.urls import path
from . import views

app_name = 'alif_user'
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('participants/list', views.participants_list, name = 'participants_list'),
    path('logout', views.logout, name = 'logout'),

     
]

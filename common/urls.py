from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('', views.admin_login, name = 'admin_login'),
    path('judges/login', views.judges_login, name = 'judges_login')

]

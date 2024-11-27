from django.urls import path
from . import views

app_name = 'alif_admin'
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('register/student', views.register_student, name = 'register_student'),
    path('generate/code-letter', views.generate_code_letter, name = 'generate_code_letter'),
    path('get/code-letter', views.get_code, name = 'get_code'),
    path('results/get', views.results, name = 'results'),
    path('result/detail/<int:id>', views.view_details, name = 'view_details'),
    path('logout', views.logout, name = 'logout')
]

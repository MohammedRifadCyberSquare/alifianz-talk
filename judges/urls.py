from django.urls import path
from . import views

app_name = 'judges'
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('participant/list', views.participant_list, name = 'participant_list'),
    path('participant/mark/<int:id>', views.mark, name = 'mark'),
    path('participant/mark/list', views.my_marks, name = 'my_marks'),

    path('logout', views.logout, name = 'logout'),
    
]

from django.urls import path
from . import views

app_name = 'pomesite'


urlpatterns = [
    path('',views.index,name='index'),
    path('lunbo',views.lunbo,name='lunbo'),
]
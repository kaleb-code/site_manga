from django.urls import path
from site_home import views

app_home = 'home'

urlpatterns = [
    path('',views.index,name='index')
]

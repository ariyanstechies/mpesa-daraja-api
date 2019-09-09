from django.urls import path
from b2c import views

urlpatterns = [
    path('', views.index,name='home'),
    path('b2c', views.b2c,name='b2c'),
]

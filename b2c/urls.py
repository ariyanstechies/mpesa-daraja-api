from django.urls import path
from b2c import views

urlpatterns = [
    path('', views.index,name='home'),
    path('b2c', views.b2c,name='b2c'),
    path('api/b2c_results', views.process_b2c_callback, name='process_b2c_callback'),
]

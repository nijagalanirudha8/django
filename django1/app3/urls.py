from django.urls import path
from . import views

urlpatterns=[
    path('multiplication/<int:num>',views.mul_table,name='mul table'),
    
]
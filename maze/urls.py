from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    # ex: /polls/5/
    path('<str:size>/', views.small, name='small'),
    
]
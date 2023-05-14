from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="index"),
    path('generate', views.generate, name="generate"),
    path('<str:pk>', views.show, name='show'),
]

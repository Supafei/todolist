from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tasks/<int:pk>/<int:status>/', views.index, name="index"),

    path('tasks/<int:pk>/', views.onetask, name="detail"),
]

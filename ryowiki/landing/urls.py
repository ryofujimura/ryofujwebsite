from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('tab1/', views.tab1, name='tab1'),
]

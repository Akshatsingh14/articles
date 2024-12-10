from django.urls import path
from . import views

urlpatterns = [
    path('',views.display),
    path('one/<int:pk>',views.detail, name = 'detail')
]
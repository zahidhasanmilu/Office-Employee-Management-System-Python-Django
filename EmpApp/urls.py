from django.urls import path
from .import views

urlpatterns = [

    path('', views.home),
    path('view_all_emp/', views.allemp, name='allemp')
]

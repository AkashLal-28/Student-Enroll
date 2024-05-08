from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update_, name="update")
]
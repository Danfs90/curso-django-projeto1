from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.home),  # Home
    path('insert/<int:id>/', views.insert),  # Insert

]

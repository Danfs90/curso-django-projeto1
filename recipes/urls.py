from django.urls import path

from recipes import views

app_name = 'insert'

urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('insert/<int:id>/', views.insert, name='insert'),  # Insert

]

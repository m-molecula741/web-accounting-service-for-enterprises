from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('addincome/', views.AddIncome.as_view()),
    path('addexpense/', views.AddExpenses.as_view()),
    path('info/', views.Info.as_view()),
]
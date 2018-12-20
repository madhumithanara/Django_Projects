from django.urls import path
from . import views

urlpatterns = [
    path('', views.Applicant_list, name='Applicant_list'),
    path('Applicant/<int:pk>/', views.Applicant_detail, name='Applicant_detail'),
    path('Applicant/new/', views.Applicant_new, name='Applicant_new'),
]
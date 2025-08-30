from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Main page
    path('process_pdfs/', views.process_pdfs, name='process_pdfs'),  # PDF processing
    path('ask_question/', views.ask_question, name='ask_question'),  # Question handling
]

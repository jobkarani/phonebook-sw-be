from django.urls import path
from app import views

urlpatterns = [
    path('contacts/', views.contacts, name='contacts' ),
    path('contactdetails/<int:contact_id>/', views.contactDetails, name='contactDetails' ),
]

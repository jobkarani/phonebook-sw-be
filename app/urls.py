from django.urls import path
from app import views

urlpatterns = [
    path('contacts/', views.contacts, name='contacts' ),
    path('contactdetails/<int:contact_id>/', views.contactDetails, name='contactDetails' ),
    path('contacts/create/', views.createContact, name='createContact'),
    path('contacts/<int:contact_id>/update/', views.updateContact, name='updateContact'),
    path('contacts/<int:contact_id>/delete/', views.deleteContact, name='deleteContact'),
]

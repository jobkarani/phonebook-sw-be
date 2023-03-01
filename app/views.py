from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# Create your views here


@api_view(['GET',])
def contacts(request):
    if request.method == "GET":
        contacts = Contact.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(contacts, request)

        # Serialize the result page
        serializer = ContactSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def contactDetails(request, contact_id):
    if request.method == "GET":
        contact= Contact.objects.filter(id = contact_id)
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)
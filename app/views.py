from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.models import *
from .serializer import *


# Create your views here

# CREATE operations
@api_view(['POST'])
def contact_create(request):
    if request.method == "GET":
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

#  READ operations

@api_view(['GET',])
def contacts(request):
    if request.method == "GET":
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def contactDetails(request, contact_id):
    if request.method == "GET":
        contact= Contact.objects.filter(id = contact_id)
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)


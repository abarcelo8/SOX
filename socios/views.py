from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Socio
from .serializers import SocioSerializer

@api_view(['POST'])
def crear_socio(request):
    serializer = SocioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def modificar_socio(request, dni):
    socio = get_object_or_404(Socio, dni=dni)
    serializer = SocioSerializer(socio, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def obtener_socios(request):
    socios = Socio.objects.all()
    serializer = SocioSerializer(socios, many=True)
    return Response(serializer.data)

# Create your views here.

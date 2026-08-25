from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cancion

def home(request, nombre=None):
    return render(request,'home.html')

def canciones(request):
    canciones = Cancion.objects.all()
    return render(request,'canciones.html',{'canciones':canciones})

def detalles_cancion(request,cancion_id):
    cancion = get_object_or_404(Cancion,id=cancion_id)
    # Obtiene la canción anterior y siguiente basándose en el ID
    cancion_anterior = Cancion.objects.filter(id__lt=cancion.id).order_by('-id').first()
    cancion_siguiente = Cancion.objects.filter(id__gt=cancion.id).order_by('id').first()

    context = {
        'cancion': cancion,
        'cancion_anterior_id': cancion_anterior.id if cancion_anterior else None,
        'cancion_siguiente_id': cancion_siguiente.id if cancion_siguiente else None,
    }
    
    return render(request, 'cancion.html', context)

# Create your views here.

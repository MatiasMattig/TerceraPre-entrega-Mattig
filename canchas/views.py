from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm

def registrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_lista')
    else:
        form = ReservaForm()
    return render(request, 'canchas/reserva_form.html', {'form': form})

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'canchas/reserva_lista.html', {'reservas': reservas})

def buscar_reservas(request):
    query = request.GET.get('q')
    if query:
        reservas = Reserva.objects.filter(cancha__nombre__icontains=query)
    else:
        reservas = Reserva.objects.all()
    return render(request, 'canchas/buscar_reservas.html', {'reservas': reservas, 'query': query})

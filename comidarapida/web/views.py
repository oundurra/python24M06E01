from django.shortcuts import render, HttpResponseRedirect
from web.forms import VentaForm
from web.models import Venta
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method =='POST':
        form = VentaForm(request.POST)

        if form.is_valid():
            contact_form = Venta.objects.create(**form.cleaned_data)
            messages.success(request, "Your data has been saved!")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Your data has not been saved!")
            return HttpResponseRedirect('/')
    else:
        form = VentaForm()
        
    return render(request, 'index.html', {'form': form})

def listado(request):
    ventas = Venta.objects.all()
    return render(request, 'listado.html', {'ventas': ventas})

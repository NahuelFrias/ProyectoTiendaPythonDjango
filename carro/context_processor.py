# este context_processor debo agregarlo en settings para que sea "total" una variable global accesible desde cualquier lugar

from .carro import Carro

def importe_total(request):
    total=0
    carro = Carro(request)
    # comento este if porque no tengo un sistema de auntentificacion
    # if request.user.is_authenticated:
    for key, value in request.session["carro"].items(): # por cada elemento en el carro
        total=total+float(value["precio"])# sumo el precio al total, segun la cantidad agregada
    return {"importe_total":total}
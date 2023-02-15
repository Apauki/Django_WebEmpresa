from .models import Link


def context_dict(request):
    context = {}
    # cargar lista de redes sociales
    links = Link.objects.all()
    # agregar al diccionario
    for link in links:
        context[link.key] = link.url # llenando el diccionario vacío
    return context 

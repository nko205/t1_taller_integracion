from django.http import HttpResponse
from django.shortcuts import render
from tarea1ti_api.req import *



def home(request): ## primera vista
    context = {}
    lista_valores = get_all_episodes()
    context["lista_valores"] = lista_valores
    return render(request, "home.html", context)

def episodios(request, id):
    context = {}
    lista_valores = info_episodio(id)
    context["lista_valores"] = lista_valores
    return render(request, "episodes.html", context)

def characters(request, id):
    context = {}
    lista_valores = info_personaje(id)
    context["lista_valores"] = lista_valores
    return render(request, "characters.html", context)

def lugares(request, id):
    context = {}
    lista_valores = info_lugar(id)
    context["lista_valores"] = lista_valores
    return render(request, "location.html", context)

from typing import Any
from django.db.models.query import QuerySet
from django.views import View, generic
from django.shortcuts import render
from django.http import Http404, HttpResponse
from datetime import datetime

from .models import Excursion, Exhibit, Exhibition, Exposition, Hall

def index(request):
    now = datetime.now()

    return render(
        request,
        "museum/index.html",
        {
            'title' : " Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "museum/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )


class ExcursionListView(generic.ListView):
    model = Excursion

    context_object_name = 'excursion_list'

    template_name = 'museum/excursion.html'
    
class HallListView(generic.ListView):
    model = Hall

    context_object_name = 'hall_list'

    template_name = 'museum/hall.html'

    # ПОМНИ КАК ОБРАЩАТЬСЯ К ПОЛЯМ FOREIGNKEY!
    # def get_queryset(self) -> QuerySet[Any]:
    #     for hall in Hall.objects.all():
    #         print(hall.exhibit.all())
    #     return super().get_queryset()

class HallExibitDetailView(View):
    @staticmethod
    def get(request, id):
        try:
            hall = Hall.objects.filter(id = id).first()

        except:
            raise Http404("Hall doesn't exist")
        
        return render(request, 'museum/exhibits.html', context={'exhibits' : Exhibit.objects.filter(hall= hall), })
        
        
class ExpositionListView(generic.ListView):
    model = Exposition

    context_object_name = 'exposition_list'

    template_name = 'museum/exposition.html'

    def get_queryset(self) -> QuerySet[Any]:
        print(Exhibit.objects.filter(exposition= Exposition.objects.get(id = 1)))
        return super().get_queryset()

class ExhibitionListView(generic.ListView):
    model = Exhibition

    context_object_name = 'exhibition_list'

    template_name = 'museum/exhibition.html'

class ExpositionExibitDetailView(View):
    @staticmethod
    def get(request, id):
        try:
            exposition = Exposition.objects.get(id = id)

        except:
            raise Http404("Exposition doesn't exist")
        
        print(Exhibit.objects.filter(exposition= exposition))
        return render(request, 'museum/exhibits.html', context={'exhibits' : Exhibit.objects.filter(exposition= exposition), })
    
    
class ExhibitionExibitDetailView(View):
    @staticmethod
    def get(request, id):
        try:
            exhibition = Exhibition.objects.get(id = id)

        except:
            raise Http404("Exhibition doesn't exist")
        
        return render(request, 'museum/exhibits.html', context={'exhibits' : Exhibit.objects.filter(exhibition= exhibition), })





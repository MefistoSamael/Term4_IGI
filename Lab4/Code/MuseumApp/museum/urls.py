
from django.urls import path, re_path
import museum.views


urlpatterns = [

    path('museum/', museum.views.index, name='index'),
    path('home/', museum.views.index, name='home'),
    path('about/', museum.views.about, name='about'),
    path('hall/', museum.views.HallListView.as_view(), name='hall'),
    path('excursion/', museum.views.ExcursionListView.as_view(), name='excursion'),
    path('exposition/', museum.views.ExpositionListView.as_view(), name='exposition'),
    path('exhibition/', museum.views.ExhibitionListView.as_view(), name='exhibition'),
    path('hall/exhibits/<int:id>/', museum.views.HallExibitDetailView.as_view(),name='hall_exhibits'),
    path('exposition/exhibits/<int:id>/', museum.views.ExpositionExibitDetailView.as_view(),name='exposition_exhibits'),
    path('exhibition/exhibits/<int:id>/', museum.views.ExhibitionExibitDetailView.as_view(),name='exhibition_exhibits'),


]

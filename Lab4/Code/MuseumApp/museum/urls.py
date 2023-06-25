
from django.urls import include, path, re_path
import museum.views


urlpatterns = [

    path('home/', museum.views.HomeView.as_view(), name='home'),
    path('about/', museum.views.about, name='about'),
    path('hall/', museum.views.HallListView.as_view(), name='hall'),
    path('excursion/', museum.views.ExcursionListView.as_view(), name='excursion'),
    path('exposition/', museum.views.ExpositionListView.as_view(), name='exposition'),
    path('exhibition/', museum.views.ExhibitionListView.as_view(), name='exhibition'),
    path('hall/exhibits/<int:id>/', museum.views.HallExibitDetailView.as_view(),name='hall_exhibits'),
    path('exposition/exhibits/<int:id>/', museum.views.ExpositionExibitDetailView.as_view(),name='exposition_exhibits'),
    path('exhibition/exhibits/<int:id>/', museum.views.ExhibitionExibitDetailView.as_view(),name='exhibition_exhibits'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/',museum.views.UserAccountView.as_view(), name='user_account' ),
    path('user/exhibits/', museum.views.EmployeeExhibitDetailView.as_view(),name='user_exhibits'),
    path('info/', museum.views.InfoView.as_view(), name='info'),
    path('diagram/', museum.views.DiagramView.as_view(), name='diagram'),

]

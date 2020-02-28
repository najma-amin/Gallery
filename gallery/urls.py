from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views     


urlpatterns=[
    url(r'^$', views.initial, name='initial'),   
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\w+)', views.specific_location, name='specific_location')
]

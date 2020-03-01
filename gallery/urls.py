from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


from . import views     
#access our views

urlpatterns=[
    url(r'^$', views.today(), name='today'),        
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\w+)', views.specific_location, name='specific_location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
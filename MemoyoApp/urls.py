from .views import *
from . import views_aj
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


web_urls = [
	path('', index, name='index'),
]

ajax_urls = [
]

# urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [*web_urls, *ajax_urls]
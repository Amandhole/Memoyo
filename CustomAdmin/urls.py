from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views_aj import *


web_urls = [
   	path('', login, name='login'),
    path('index/', index, name='index'),
   	path('registration/', registration, name='registration'),  # registration form
   	  # login form
]

ajax_urls = [
    # path('Registration_Ajax/', Registration_Ajax, name='Registration_Ajax'),
    # path('LoginAjax/', LoginAjax, name='LoginAjax'),
    # path('logoutAjax/', logoutAjax, name='logoutAjax')
]

# urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [*web_urls, *ajax_urls]

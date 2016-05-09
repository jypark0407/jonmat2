from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from jonmat.views.index import index
from .views.congress_member import congress_member_list, congress_member_detail
from .views.restaurant import restaurant_list, restaurant_detail


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index),
    url(r'^who/$', congress_member_list, name='congress_member_list'),
    url(r'^who/([0-9]+)$', congress_member_detail, name='congress_member_detail'),
    url(r'^where/$', restaurant_list, name='restaurant_list'),
    url(r'^where/([0-9]+)$', restaurant_detail, name='restaurant_detail'),
]

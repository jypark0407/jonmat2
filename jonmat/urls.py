from django.conf import settings
from django.conf.urls import url
from django_distill import distill_url as surl
from django.conf.urls.static import static
from django.contrib import admin
from jonmat.views.index import index, index_distill_func
from .views.congress_member import (
    congress_member_list,
    congress_member_detail,
    congress_member_list_distill_func,
    congress_member_detail_distill_func,
)
from .views.restaurant import (
    restaurant_list,
    restaurant_detail,
    restaurant_list_distill_func,
    restaurant_detail_distill_func,
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    surl(
        r'^$',
        index,
        name='index',
        distill_func=index_distill_func,
        distill_file='index.html'
    ),
    surl(
        r'^who/$',
        congress_member_list,
        name='congress_member_list',
        distill_func=congress_member_list_distill_func,
        distill_file='who/index.html'
    ),
    surl(
        r'^who/([0-9]+)$',
        congress_member_detail,
        name='congress_member_detail',
        distill_func=congress_member_detail_distill_func,
    ),
    surl(
        r'^where/$',
        restaurant_list,
        name='restaurant_list',
        distill_func=restaurant_list_distill_func,
        distill_file='where/index.html',
    ),
    surl(
        r'^where/([0-9]+)$',
        restaurant_detail,
        name='restaurant_detail',
        distill_func=restaurant_detail_distill_func,
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

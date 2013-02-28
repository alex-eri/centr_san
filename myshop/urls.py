__author__ = 'eri'
from django.conf.urls import *
from shop import urls as shop_urls


urlpatterns = patterns('',
                       url(r'^catalog/', include('shop_categories.urls')),
                       # url(r'^checkout/confirm/$', MyOrderConfirmView.as_view(), name='checkout_shipping'),
                       (r'^', include(shop_urls)),  # <-- That's the important bit
)
from django.conf.urls import url
from .views import index_view, stats_view, CreateOfferView,UpdateOfferView,DeleteOfferView,DetailOfferView


urlpatterns = [
    url(r'^create/$', CreateOfferView.as_view(), name='create-offert'),
    url(r'^offer/edit/(?P<offer>[0-9]+)', UpdateOfferView.as_view(), name='edit-offer'),
    url(r'^offer/detail/(?P<offer>[0-9]+)', DetailOfferView.as_view(), name='detail-offer'),
    url(r'^delete/(?P<pk>[0-9]+)$', DeleteOfferView.as_view(), name='delete-offer'),
    url(r'^stats/$', stats_view, name='stats'),
    url(r'^$', index_view.as_view(), name='index')

]


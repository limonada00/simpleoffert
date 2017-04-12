from django.conf.urls import url
from .views import index_view, CreateOfferView, UpdateOfferView, DeleteOfferView, DetailOfferView, StatsView, PendingOffersView, ApprovedAndRejectedView
from .views import index_view, CreateOfferView, UpdateOfferView, DeleteOfferView, DetailOfferView, StatsView


urlpatterns = [
    url(r'^create/$', CreateOfferView.as_view(), name='create-offert'),
    url(r'^offer/edit/(?P<offer>[0-9]+)', UpdateOfferView.as_view(), name='edit-offer'),
    url(r'^offer/detail/(?P<offer>[0-9]+)', DetailOfferView.as_view(), name='detail-offer'),
    url(r'^delete/(?P<pk>[0-9]+)$', DeleteOfferView.as_view(), name='delete-offer'),
    url(r'^stats/$', StatsView.as_view(), name='stats'),
    url(r'^pending/$', PendingOffersView.as_view(), name='pending'),
    url(r'^ApprovedAndRejected/(?P<offer>[0-9]+)/(?P<status>[0-9]+)', ApprovedAndRejectedView.as_view(), name='approved-rejected'),
    url(r'^$', index_view.as_view(), name='index')

]


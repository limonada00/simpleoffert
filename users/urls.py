from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import login_view, logout_user, register_page

urlpatterns = [
   # url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
   # url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/$', register_page, name='register'),
    url(r'^$', login, name='login'),
]
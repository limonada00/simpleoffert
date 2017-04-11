from django.conf.urls import url
from django.contrib.auth.views import login, logout, LoginView
from .views import login_view, logout_user, register_page
from django.contrib.auth import views as auth_views
#from django.contrib.auth import LoginView

urlpatterns = [
   # url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
   # url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/$', register_page, name='register'),
    #url(r'^$', login, name='login'),
    url(r'^$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
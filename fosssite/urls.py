from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$',views.login,name='login'),
	url(r'^auth/$',views.auth_view,name='auth_view'),
	url(r'^loggedin/$',views.loggedin,name='loggedin'),
]

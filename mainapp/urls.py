from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^fcuk/$', views.formpage),
	url(r'^emailsubmit$', views.emailsubmit),
]

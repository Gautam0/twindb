from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^google_form/$', views.google_form),
	url(r'^emailsubmit$', views.emailsubmit),
	url(r'^invite$', views.invite),
	url(r'^thank_page$', views.thank_page),
	url(r'^thank_page2$', views.thank_page2),
	url(r'^contact$', views.contact),
]

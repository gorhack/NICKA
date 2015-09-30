from django.conf.urls import url
from . import views

urlpatterns = [
	# /codenames/index/
	url(r'^$', views.index_page, name='index_page'),
	# /
]
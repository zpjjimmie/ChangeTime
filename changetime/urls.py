from django.conf.urls import url

from . import views

app_name = 'changetime'
urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', views.ModifyView.as_view(), name='modify'),
	url(r'^/change/$', views.change, name='change'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
]

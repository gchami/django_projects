from django.conf.urls import url
from . import views

urlpatterns = [
            # ex: /polls/
            url(r'^$', views.onie, name='onie'),
            url(r'^switches/$', views.viewSwitches, name='viewSwitches'),
            url(r'^update/$', views.viewSwitches, name='editSwitches'),
              ]

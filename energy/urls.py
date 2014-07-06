from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'energy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^energyapi/', include('energyapi.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^powerof50/buildings', 'energyapi.views.powerof50buildings', name="powerof50buildings"),
    url(r'^powerof50/building/(?P<buildingId>[0-9]+)', 'energyapi.views.powerof50building', name="powerof50buildings"),
    url(r'^index', 'energyapi.views.index', name="index"),
)

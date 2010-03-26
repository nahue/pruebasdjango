from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^a/', include('a.foo.urls')),
    (r'^cuentas/', include('registration.backends.default.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$','django.views.static.serve',
    	{'document_root': settings.MEDIA_ROOT + "/tiny_mce" }),
    (r'', include('django.contrib.flatpages.urls')),
)

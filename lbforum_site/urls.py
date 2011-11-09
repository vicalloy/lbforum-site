from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from registration.views import register
from lbforum.accountviews import profile

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/register/$',
        register,
        { 'backend': 'lbregistration.backends.simple.SimpleBackend' },
        name='registration_register'),   
    url(r'^user/(?P<user_id>\d+)/$', profile, name='user_profile'),
    #(r'^accounts/avatar/', include('simpleavatar.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^attachments/', include('attachments.urls')),
    url(r'^captcha/', include('captcha.urls')),
    (r'^', include('lbforum.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

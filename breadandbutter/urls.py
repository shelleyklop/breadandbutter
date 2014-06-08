from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'breadandbutter.views.home', name='home'),
    # url(r'^breadandbutter/', include('breadandbutter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^foundation/', include('foundation.urls')),
    url(r'', include('bank.urls')),
    # User login
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'bank/login.html'}),
    # User logout
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
     # url('^register/$', CreateView.as_view(
     #        template_name='bank/register.html',
     #        form_class=UserCreationForm,
     #        success_url='/')),


)

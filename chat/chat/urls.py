from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from chat.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='homepage'),  # The start point for index view
    url(r'^accounts/login/$', login, name='login'),  # The base django login view
    url(r'^accounts/logout/$', logout, name='logout'),  # The base django logout view
    url(r'^admin/', admin.site.urls),

]

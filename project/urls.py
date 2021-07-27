"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from project.core import views as core_views

handler404 = 'project.core.views.handler404'
handler500 = 'project.core.views.handler500'

urlpatterns = [
    url('^$', core_views.index),
    path('admin/', admin.site.urls),

    path('api/v1/', include([
        # path('admin/', include('project.apps.superadmin.urls')),
        # path('vendors/', include('project.apps.vendor.urls')),
        # path('customer/', include('project.apps.customer.urls')),
        path('auth/', include('project.apps.user.urls')),
    ]))
]

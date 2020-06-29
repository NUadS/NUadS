"""Orbital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from accounts import views as accounts_views
from survey import views as survey_views
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
#     path('accounts/', include('accounts.urls')),
#     path('admin/', admin.site.urls)
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('survey.urls')),
    url(r'^$',accounts_views.index,name='index'),
    url(r'^special/',accounts_views.special,name='special'),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^accounts/profile/',accounts_views.profile_view, name='profile'),
    url(r'^logout/$', accounts_views.user_logout, name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

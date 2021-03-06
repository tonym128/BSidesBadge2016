"""BSidesBadgeServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
#from badge import views
from badge.views import badgeCheckin,badgeGetHash, badgeAddAlias, badgeAddChallenge, getBadgeDetails, getAllBadges, saveCurrentTeamStandings, RPSSL_api, aboutPage, FAQ, theGame

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'checkin/(?P<badgeID>[A-Za-z0-9]+)/$', csrf_exempt(badgeCheckin.as_view()), name='checkin'),
    url(r'gethash/(?P<badgeID>[A-Za-z0-9]+)/$', csrf_exempt(badgeGetHash.as_view()), name='gethash'),
    url(r'addalias/$', badgeAddAlias.as_view(), name='addalias'),
    url(r'addhash/$', badgeAddChallenge.as_view(), name='addhash'),
    url(r'badgeDetails/(?P<badgeID>[A-Za-z0-9]+)/$', getBadgeDetails.as_view(), name='badgeDetails'),
    url(r'RPSSL/(?P<challengerBadge>[A-Za-z0-9]+)/(?P<selection>[0-9]+)/(?P<badgeID>[A-Za-z0-9]+)/$', csrf_exempt(RPSSL_api.as_view()), name='badgeDetails'),
    url(r'listBadges/$', getAllBadges.as_view(), name='badgeDetails'),
    url(r'saveGameState/$', saveCurrentTeamStandings.as_view(), name='saveCurrentTeamStandings'),
    url(r'thegame/$', theGame.as_view(), name='thegame'),
    url(r'faq/$', FAQ.as_view(), name='faq'),
    url(r'about/$', aboutPage.as_view(), name='about'),
    #url(r'workbench/(?P<badgeID>[0-9]+)$', badgeGetHash.as_view(), name='workbench'),
    
]

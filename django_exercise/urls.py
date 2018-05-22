"""django_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.contrib import admin
from django.conf.urls import url, include

from django.contrib.auth import views as auth_views

from django_exercise.views import HomeView
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^dashboard/', include('dash_board.urls', namespace='dash_board')),






    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^login_after$', TemplateView.as_view(template_name='foo.html'), name='login_after'),


    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # url(r'^logout_kakao/$', auth_views.login, name='login'),

    url(r'^auth/', include('social_django.urls', namespace='social')),





    url(r'^admin/', admin.site.urls),
]

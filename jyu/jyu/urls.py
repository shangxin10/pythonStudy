"""jyu URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from student import views as student_views

urlpatterns = [
    url(r'^login/$',student_views.login,name='login'),
    url(r'^loginPost$',student_views.loginPost),
    url(r'^logout$',student_views.logout),
    url(r'^home$',student_views.home),
    url(r'^score',student_views.score, name='score'),
    url(r'^admin/', admin.site.urls),

]

"""shortly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.defaults import page_not_found
from django.utils.functional import curry
from appshortly import views
from django.conf.urls import include, url

handler404 = curry(page_not_found, template_name='appshortly/404.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/', views.index),
    path('', views.ShortlyView.as_view()),
    # url(r'/', views.ShortlyView.as_view()),
    path('<int:url_id>', views.RedirectByShortId.as_view()),
    path('<int:url_id>/detail', views.ShortlyView.as_view()),
    # path('<int:url_id>/detail', views.view_url),
    # path('create_short_url', views.create_new_url),

]

# -*- coding: utf-8 -*-
# 总的urls配置文件
"""mysite URL Configuration

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
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.views.generic import RedirectView
from learn import views as learn_views
from learn import forms as learn_forms
from learn.views import MyView

urlpatterns = [

    url(r'^$',learn_views.home, name='home'),
    #url(r'^$', learn_views.index),
    # http://127.0.0.1:8000/add/?a=4&b=5
    url(r'^add/$', 'learn.views.add', name='add'),
    ## url(r'^add/', calc_views.add, name='add'),  #注意修改了这一行

    url(r'^admin/', admin.site.urls),

    url(r'^add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),

    url('r^add2/(\d+)/(\d+)/$', learn_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),

    #url(r'^home1/$',learn_views.home1,name='home1')
    url(r'^home1/$', learn_views.home1, name='home1'),

    url(r'^home2/$', learn_views.home2, name='home2'),

    url(r'^from_test/$',learn_views.from_test, name="from"),

    url(r'^form/$',learn_views.form),

    url(r'^index1/$', learn_views.index1, name='index1'),

    url(r'^accounts/',include('users.urls')),

    url(r'^json/$',learn_views.json, name="json"),

    url(r'^json_demo/$', learn_views.json_demo, name="json")
]

urlpatterns = patterns['', url(r'^mine/$',MyView.as_view(), name='my_view')]

urlpatterns = patterns('',
                       url(r'^go-to-django/$',RedirectView.as_view(url='http://djangoproject.com'), name = 'go-to-django'),
                       url(r'^go-go-ziqiangxuetang/$', RedirectView.as_view(url='http://www.ziqiangxuetang.com',permanent=False,
                                                                            name='go-to-zqxt')),)

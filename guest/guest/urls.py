"""guest URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from sign import views #导入sign应用的views文件

urlpatterns = [
    url(r'^$', views.index), #定义访问存在路径为登录状态时自动返回到登录首页
    url(r'^index/$', views.index),# 添加index/路径配置
    url(r'^accounts/login/$', views.index),
    url(r'^index.html/$', views.indexhtml),# 添加index.html/路径配置
    url(r'^login_action/$', views.login_action),#添加login_action/路径配置
    url(r'^event_manage/$', views.event_manage),#添加event_manage/路径配置
    url(r'^admin/', admin.site.urls), #admin超级管理员地址
]

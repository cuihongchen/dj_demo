"""test_b URL Configuration

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
from django.urls import include,path
from test_app import views

urlpatterns = [
    #admin用户访问页面
    path('admin/', admin.site.urls),
    #seting文件中ROOT_URLCONF = 'test_b.urls'，设置为根目录url
    #然后把不同的APPURL在这里进行设置，访问不同APP的URL会进行分发操作
    path('test_app/', include('test_app.urls')),
    path('users/', include('users.urls')),
]

#为应用程序users定义URL模式

from django.urls import re_path,path
#导入登录的默认视图
from django.contrib.auth.views import LoginView
from . import views

urlpatterns =[
    #登录页面
    re_path(r'^login/$',LoginView.as_view(template_name='login.html'),name = 'login'),
    #注销页面
    re_path(r'^loguot/$',views.logout_view,name='logout_view'),
    #用户注册,由于是由test_b/urls中分发过来的，所以访问地址为
    # http://127.0.0.1:8000/users/register/，要加个当前文件的名字users
    re_path(r'^register/$',views.register,name='register'),
]
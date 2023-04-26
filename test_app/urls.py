'''定义test_app的URL模式'''
from django.urls import path,include,re_path
from . import views
from django.contrib import admin

urlpatterns = [
    #管理员访问
    path('admin/', admin.site.urls),
    #主页
    path('index/',views.index,name='index'),
    # 显示所有的主题
    path('topics/',views.topics,name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),

]
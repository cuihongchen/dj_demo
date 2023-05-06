from django.contrib import admin

# Register your models here.
from test_app.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.site_header('学习笔记')
admin.site.site_title('学习笔记')
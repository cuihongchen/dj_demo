from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.shortcuts import render
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from  django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')

#装饰器用户必须先登录才能访问topics等，否则跳转到登录页面
@login_required()
def topics(request):
    #显示所有的主题
    #topics = Topic.objects.order_by('date_added')
    #只向用户显示自己的主题
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'topics.html',context)

@login_required()
def topic(request,topic_id):
    #显示单个主题及条目
    topic = Topic.objects.get(id=topic_id)
    #渲染网页前确认当前主题属于当前用户
    if topic.owner != request.user:
        #服务器上没有请求的资源时，返回404响应
        raise Http404
    entries = topic.entry_set.order_by('date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'topic.html',context)

@login_required()
def new_topic(request):
    #添加新主题
    if request.method !='POST':
        #未提交数据，创建一个新表单
        form = TopicForm()
    else:
        #post提交的数据，对数据进行变更
        form = TopicForm(request.POST)
        if form.is_valid():
            #因为添加了数据库字段owner，因此需要将新主题关联到特定用户
            #先调用form.save，并传递实参commit=false，因为要先修改新主题的owner属性，再进行保存
            new_topic=form.save(commit=False)
            #将新主题的owner属性设置为当前用户
            new_topic.owner=request.user
            new_topic.save()
            #form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form':form}
    return render(request,'new_topic.html',context)

@login_required()
def new_entry(request,topic_id):
    #在特定的主题中添加新条目
    topic = Topic.objects.get(id = topic_id)
    if request.method !='POST':
        #未提交数据，创建一个空表单
        form = EntryForm()
    else:
        #post提交的数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'new_entry.html',context)

@login_required()
def edit_entry(request,entry_id):
    #编辑既有条目
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #和topic一样，确认当前访问用户是否为主题的拥有用户
    if topic.owner !=request.user:
        raise Http404
    if request.method !='POST':
        #初次请求，使用的当前目录条目填充表单
        form = EntryForm(instance=entry)
    else:
        #post提交的数据，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'edit_entry.html',context)
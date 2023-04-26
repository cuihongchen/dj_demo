from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm #注册表单
# Create your views here.
def logout_view(request):
    #注销用户
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    #注册新用户
    if request.method !='POST':
        #显示空的注册表单
        form = UserCreationForm()
    else:
        #处理填写好的表单
        form = UserCreationForm(data=request.POST)

        #检查数据是否有效，包含非法字符，两次密码是否一致等
        if form.is_valid():
            #数据有效，存储到数据库，并命名为新用户
            new_user = form.save()
            #让用户自动登录注册，再重定向到主页
            authenticate_user= authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form':form}
    return render(request,'register.html',context)

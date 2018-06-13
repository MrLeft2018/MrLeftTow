from django.http import HttpResponse, HttpResponseRedirect, response #调用返回方法
from django.shortcuts import render #引用render方法返回
from django.contrib import auth #引用数据库表单
from django.contrib.auth.decorators import login_required #限制视图调用权限必须登录才能访问
from sign.models import Event

# Create your views here.
def index(request):
   # return HttpResponse("Hello Django!")
   return render(request, "index.html")
def indexhtml(requesthtml):
    return render(requesthtml, "index.html")

#登录函数
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        #if username == 'admin' and password == 'admin123':#写死的判断验证登录用户名和密码是否正确
            #return HttpResponse('login success!')#登录成功后通过HTTPResponse方法直接返回成功信息
            #return HttpResponseRedirect('/event_manage/')#登录成功后通过HTTPResponseRedirect方法跳转到成功登录页面
            #response.set_cookie('user', username, 3600)#添加浏览器cookie
            #引用Django验证登录
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) #登录
            request.session['user'] = username #将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
#签到查询
@login_required
def event_manage(request):
    event_list = Event.object.all()
    #username = request.COOKIES.get('user', '')#读取浏览器cookie
    username = request.session.get('user', '')#读取浏览器session
    return render(request, "event_manage.html", {"user": username,"events": event_list})

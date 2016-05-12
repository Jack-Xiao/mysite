#coding:utf-8
import hashlib

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str, python_2_unicode_compatible
from django.views.decorators.cache import cache_page
import json
from django.shortcuts import render
from django.views.generic import View, TemplateView
from model_utils.tests.models import Article
from pip._vendor.html5lib.treewalkers import etree

WEIXIN_TOKEN = 'write-a-value'

@cache_page(60 * 15)
def index(request):
    return HttpResponse(u"欢迎光临！")

#render 给予
def home(request):
    string = u'承担测测测测测测测测'
    return render(request, 'learn/home.html', {'string': string})

def add(request):
    a = request.GET['a']
    # a = request.GET.get('a',0)
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

#该url 重定向到 add 方法.  reverse--翻转, redirect 重定向
def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )

def home1(request):
    List = map(str,range(100)) # 一个长度为100的 List
    return render(request, 'learn/home1.html', {'List': List})

def home2(requst):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(requst, 'learn/home2.html', {'TutorialList' : TutorialList})

def from_test(requst):
    return render(requst,'learn/from_test.html')

# def form_test(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     a = int(a)
#     b = int(b)
#     return HttpResponse(str(a+b))

def form(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

##def .form import forms.A
from .forms import AddForm

def post_demo(request):
    if request.method == 'POST':
        form = AddForm(request.POST) #form 包含提交的数据
        if form.is_valid(): #如果提交的数据合法
            # a = form.cleaned_data['a']
            # b = form.cleaned_data['b']
            return HttpResponse(".......................aaa____")
    else: #正常访问时
            form = AddForm()

    return render(request, 'learn/index.html', {'form': form})


#django的表单提交
def index1(request):
    if request.method == 'POST':
        form = AddForm(request.POST) #form 包含提交的数据
        if form.is_valid(): #如果提交的数据合法
            # a = form.cleaned_data['a']
            # b = form.cleaned_data['b']
            return HttpResponse(".......................aaa____")
    else: #正常访问时
            form = AddForm()

    return render(request, 'learn/index1.html', {'form': form})

# def post_comment(request,new_commnet):
#     if request.session.get('has_commented',False):
#         return HttpResponse("You're already commented.")
#
#     c = comments.Comment(comment = new_commnet)
#     c.save()
#     request.session['has_commented'] = True
#     return HttpResponse('Thanks for your comment!')
#
# def login(request):
#     m = Member.objects.get(username = request.POST['username'])
#     if m.password == request.POST['password']:
#         request.session['member_id'] = m.id
#         return HttpResponse("You're logged in.")
#     else:
#         return HttpResponse("Your username and password didn't match.")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def json(request):
    List = ['自强学堂','json模板']
    Dict = {'sit' : 'ziqiang', 'author' : 'zhongzhong'}
    return render(request,'json.html',{
        'List': json.dump(List),
        'Dict': json.dump(Dict)
    })

#JsonResponse  --- json 对象
def json_demo(request):
    List = ['自强学堂','json模板']
    Dict = {'sit' : 'ziqiang', 'author' : 'zhongzhong'}
    return JsonResponse(Dict)


class MyView(View):
    def get(self,request, *args,**kwargs):
        return HttpResponse('Hello, World!')


class HomePageView(TemplateView):
    template_name = "h.html"
    def get_context_data(self,**kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

@python_2_unicode_compatible
def weixin_main(request):
    """
    所有的消息都会先进入这个函数进行处理，函数包含两个功能，
    微信接入验证是GET方法，
    微信正常的收发消息是用POST方法。
    """
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")
    else:
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        response = request_xml
        #response_xml = auto_reply_main(request_xml)# 修改这里
        #return HttpResponse(response_xml)

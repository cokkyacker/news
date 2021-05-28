from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from article.form import ArticleForm

# Create your views here.
from article.models import ArticleType, Article
from lib.lib import my_md5

def index(request):
    types = ArticleType.objects.all()
    # return render(request, 'frontpage/index.html', {'types': types})
    return render(request, 'frontpage/index.html', locals())


def articleType(request):

    types = ArticleType.objects.all()
    articletypeid = request.GET.get('articletypeid', None)
    articles = Article.objects.filter(type_id=articletypeid)


    # 1,生成Paginator对象
    paginator = Paginator(articles, 5)
    # 2,告诉paginator，当前处在哪一页上
    pagenum = request.GET.get('pagenum')
    try:
        post = paginator.page(pagenum)
    except PageNotAnInteger as e:
        pagenum = 1
        post = paginator.page(pagenum)

    r = paginator.page_range
    print(r[0])
    print(r[-1])

    head = int(pagenum)-2
    tailer = int(pagenum)+3

    if head<=0:
        head =1
    if tailer > r[-1]:
        tailer = r[-1]+1
    pages = range(head, tailer)


    return render(request, 'frontpage/articletype.html', locals())






def datacreate(request):
    for i in range(100):
        Article.objects.create(**{
            'title': '自动添加的文章标题，当前序号为：'+str(i),
            'content': '1234567890',
            'type_id': 1,
            'author_id': request.session['userid']
        })
    return HttpResponse("ok")


def article(request):
    articleid = request.GET.get('articleid')
    article = Article.objects.filter(id=articleid)[0]

    return render(request, 'frontpage/article.html', locals())


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        pw = my_md5(password)
        
    types = ArticleType.objects.all()
    return render(request, 'frontpage/login.html', locals())


def about(request):

    # if request.method== 'GET':
    #     # types = ArticleType.objects.all()
    #     af = ArticleForm()
    #     return render(request, '/', {'af': af})
    # else:
    #     af = ArticleForm(request.POST)
    #     if af.is_valid():
    #         data = af.cleaned_data
    #         name = data['name']
    #         data['name'] = ArticleType.objects.filter(username=name)[0]
    #         tel = data['tel']
    #         data['tel'] = ArticleType.objects.filter(tel=tel)[0]
    #         email = data['email']
    #         data['email'] = ArticleType.objects.filter(email=email)[0]
    #         leaveword = data['leaveword']
    #         data['leaveword'] = ArticleType.objects.filter(leaveword=leaveword)[0]
    #         Article.objects.create(**data)
    #
    #         return render(request, 'sucess.html',
    #                       {
    #                           'info': '恭喜你，留言已经成功添加！',
    #                           'url': '/frontpage/about/'
    #                       })
    #     else:
    #         print(af.errors)
    #         return HttpResponse("error")
    return render(request, 'frontpage/about.html', locals())



def footer1(request):
    types = ArticleType.objects.all()
    articles = Article.objects.filter(id=308)
    # 1,生成Paginator对象
    paginator = Paginator(articles, 5)
    # 2,告诉paginator，当前处在哪一页上
    pagenum = request.GET.get('pagenum')
    try:
        post = paginator.page(pagenum)
    except PageNotAnInteger as e:
        pagenum = 1
        post = paginator.page(pagenum)

    r = paginator.page_range
    print(r[0])
    print(r[-1])

    head = int(pagenum)-2
    tailer = int(pagenum)+3

    if head<=0:
        head =1
    if tailer > r[-1]:
        tailer = r[-1]+1
    pages = range(head, tailer)
#    orders = Article.objects.order_by(-id)
    return render(request, 'frontpage/footer1.html', locals())


def footer2(request):
    types = ArticleType.objects.all()
    articles = Article.objects.filter(id=310)
    # 1,生成Paginator对象
    paginator = Paginator(articles, 5)
    # 2,告诉paginator，当前处在哪一页上
    pagenum = request.GET.get('pagenum')
    try:
        post = paginator.page(pagenum)
    except PageNotAnInteger as e:
        pagenum = 1
        post = paginator.page(pagenum)

    r = paginator.page_range
    print(r[0])
    print(r[-1])

    head = int(pagenum) - 2
    tailer = int(pagenum) + 3

    if head <= 0:
        head = 1
    if tailer > r[-1]:
        tailer = r[-1] + 1
    pages = range(head, tailer)
    #    orders = Article.objects.order_by(-id)
    return render(request, 'frontpage/footer2.html', locals())


def footer3(request):
    types = ArticleType.objects.all()
    articles = Article.objects.filter(id=309)
    # 1,生成Paginator对象
    paginator = Paginator(articles, 5)
    # 2,告诉paginator，当前处在哪一页上
    pagenum = request.GET.get('pagenum')
    try:
        post = paginator.page(pagenum)
    except PageNotAnInteger as e:
        pagenum = 1
        post = paginator.page(pagenum)

    r = paginator.page_range
    print(r[0])
    print(r[-1])

    head = int(pagenum) - 2
    tailer = int(pagenum) + 3

    if head <= 0:
        head = 1
    if tailer > r[-1]:
        tailer = r[-1] + 1
    pages = range(head, tailer)
    #    orders = Article.objects.order_by(-id)
    return render(request, 'frontpage/footer3.html', locals())
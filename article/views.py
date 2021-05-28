from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.form import ArticleForm
from article.models import ArticleType, Article
from login.models import Users


def articlelist(request):
    articles = Article.objects.all()
    return render(request, 'article-list.html', {'articles': articles})


def articleadd(request):
    if request.method== 'GET':
        # types = ArticleType.objects.all()
        af = ArticleForm()
        return render(request, 'article-add.html', {'af': af})
    else:
        # title = request.POST.get('articletitle')
        # type = request.POST.get('articletype')
        # content = request.POST.get('content')
        # author = request.session.get('userid')
        #
        # print(title)
        # print(type)
        # print(content)
        # print(author)
        #
        # article = Article()
        # article.title = title
        # article.type = ArticleType.objects.filter(id=type)[0]
        # article.content = content
        # article.author = Users.objects.filter(id=author)[0]
        # article.save()

        af = ArticleForm(request.POST)
        if af.is_valid():
            data = af.cleaned_data
            typeid = data['type']
            data['type'] = ArticleType.objects.filter(id=typeid)[0]
            author = request.session.get('userid')
            data['author'] = Users.objects.filter(id=author)[0]

            Article.objects.create(**data)
            return render(request, 'sucess.html',
                          {
                              'info': '恭喜你，文章已经成功添加！',
                              'url': '/article/articlelist/'
                          })
        else:
            print(af.errors)
            return HttpResponse("error")



def init(request):
    try:
        ArticleType(title='时政类').save()
        ArticleType(title='财经类').save()
        ArticleType(title='娱乐类').save()
    except:
        return HttpResponse('初始化失败，文章类型已完成过初始化！')
    return HttpResponse('ok')


def articleedit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        article = Article.objects.filter(id=id)[0]
        # types = ArticleType.objects.all()
        # return render(request, 'article-edit.html', {'article': article, 'types': types})

        af = ArticleForm(initial={
            'title': article.title,
            'type': article.type.id,
            'content': article.content
        })
        return render(request, 'article-add.html', {'af': af, 'id': id})
    else:
        id = request.POST.get('id')
        # typeid = request.POST.get('articletype')
        # title = request.POST.get('articletitle')
        # content = request.POST.get('content')
        # type = ArticleType.objects.filter(id=typeid)[0]
        #
        # article = Article.objects.filter(id=id)[0]
        # article.title = title
        # article.content = content
        # article.type = type
        # article.save()

        af = ArticleForm(request.POST)
        if af.is_valid():
            data = af.cleaned_data
            typeid = data['type']
            data['type'] = ArticleType.objects.filter(id=typeid)[0]
            Article.objects.filter(id=id).update(**data)
            return render(request, 'sucess.html',
                          {
                              'info': '恭喜你，文章已经成功修改！',
                              'url': '/article/articlelist/'
                          })
        else:
            print(af.errors)
            return HttpResponse("error")




def articledel(request):
    id = request.POST.get('id')
    article = Article.objects.filter(id=id)[0]
    try:
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")
    # return None


def testadd(request):
    af = ArticleForm()
    return render(request, 'testadd.html', {'af': af})
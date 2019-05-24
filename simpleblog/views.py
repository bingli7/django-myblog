from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Article


def blog_index(request):
    # 获取所有Article
    articles = Article.objects.all()

    # render(request, template_name, context)
    # 注意：
    # context是字典dict
    # dict中key为字符串
    return render(request, template_name='simpleblog/index.html', context={'articles': articles})


# article_id对应urls中的参数
def article_page(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, template_name='simpleblog/article_page.html', context={'article': article})


def edit_page(request, article_id):
    # article_id为0，新建博客, 注意char到int转换
    if int(article_id) == 0:
        return render(request, template_name='simpleblog/edit_page.html')
    else:
        # 编辑已有博客
        article = Article.objects.get(id=article_id)
        return render(request, template_name='simpleblog/edit_page.html', context={'article': article})


def edit_action(request):

    article_id = request.POST['article_id']
    new_title = request.POST['title']
    new_content = request.POST['content']
    # article_id为0，新建博客
    if int(article_id) == 0:
        new_article=Article.objects.create(title=new_title, content=new_content)
        return HttpResponseRedirect(reverse('simpleblog:article_page', args=(new_article.id, )))
    else:
        # 编辑已有博客
        article = Article.objects.get(id=article_id)
        article.title = new_title
        article.content = new_content
        article.save()
        # reverse(namespace:name, url参数列表)
        return HttpResponseRedirect(reverse('simpleblog:article_page', args=(article_id, )))

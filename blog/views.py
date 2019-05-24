from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/article_page.html', {"article": article})


def article_edit(request, article_id):
    # New article
    if int(article_id) == 0:
        return render(request, 'blog/article_edit_page.html')
    else:
        # edit an existed article
        article = Article.objects.get(id=article_id)
        return render(request, 'blog/article_edit_page.html', {'article': article})


def edit_action(request):
    article_id = request.POST['article_id']
    title = request.POST['title']
    content = request.POST['content']

    # new article
    if int(article_id) == 0:
        new_article = Article.objects.create(title=title, content=content)
        return HttpResponseRedirect(reverse('blog:article_page', args=(new_article.id,)))
    else:
        # edit existed article
        article = Article.objects.get(id=article_id)
        article.title = title
        article.content = content
        article.save()
        return HttpResponseRedirect(reverse('blog:article_page', args=(article_id,)))

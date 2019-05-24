from django.db import models


class Article(models.Model):
    title = models.CharField('标题', max_length=200)
    content = models.TextField('内容', default='blog content')
    pub_date = models.DateTimeField('发表时间', auto_now=True)

    def __str__(self):
        return self.title

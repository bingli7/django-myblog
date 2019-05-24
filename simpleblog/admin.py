from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    # 显示列
    list_display = ('title', 'content', 'pub_date')
    # 过滤项
    list_filter = ('pub_date',)


admin.site.register(Article, ArticleAdmin)

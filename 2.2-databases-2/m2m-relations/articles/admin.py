from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags

class ArticleTagsM2MInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'articles')

class ArticleTagsM2MInline(admin.TabularInline):
    model = Article.tags.through
    formset = ArticleTagsM2MInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsM2MInline]


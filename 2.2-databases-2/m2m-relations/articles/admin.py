from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags

class ArticleTagsM2MInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter_topics = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                counter_topics += 1

        if counter_topics == 0:
            raise ValidationError('Выберите основной раздел статьи')
        if counter_topics > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()

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


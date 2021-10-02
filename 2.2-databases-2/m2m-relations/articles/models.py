from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField('Tags', blank=True, through='TagArticleM2M')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str(self):
        return self.name


class TagArticleM2M(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.PROTECT, related_name='t1')
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='t1')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tag}_{self.article}'

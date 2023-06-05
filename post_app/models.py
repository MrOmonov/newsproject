from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class PostModel(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft',
        Published = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField()
    text = models.TextField()
    image = models.ImageField(upload_to='post/images')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    published_time = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', args=[self.slug])

    class Meta:
        ordering = ['-published_time']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категори'

class Contact(models.Model):
    name = models.CharField(max_length=150)
    e_mail = models.EmailField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
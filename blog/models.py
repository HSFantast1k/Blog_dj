from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from turtle import title
from django.db import models
from django.urls import reverse

# Create your models here.
'''
Category 
============
title, slug 

Tag
============
title, slug

Post
============
title, slug, author, content, created_at, photo, views, category, tags 
'''


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255,
                            verbose_name='Url категории',
                            unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория (ю)'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название тега')
    slug = models.SlugField(max_length=50,
                            verbose_name='Url тега',
                            unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    slug = models.SlugField(max_length=255,
                            verbose_name='Url поста',
                            unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Опубликоваано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',
                              blank=True,
                              verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name='posts',
                                 verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

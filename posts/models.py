from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='PB')

    def delete(self, id):
        return super().get_queryset().filter(id=id).update(status='DF')


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.PUBLISHED,
    )
    objects = models.Manager()
    published = CustomManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        ordering = ['-publish']

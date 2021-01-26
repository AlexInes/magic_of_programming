from django.db import models
from ckeditor.fields import RichTextField


class Tool(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"


class Image(models.Model):
    url = models.URLField()
    alt_text = models.CharField(max_length=50)

    def __str__(self):
        return self.alt_text

    class Meta:
        ordering = ['alt_text']


class Project(models.Model):
    title = models.CharField(max_length=70)
    categories = models.ManyToManyField(Category)
    tools = models.ManyToManyField(Tool)
    short_description = models.CharField(max_length=150)
    description = RichTextField()
    source_url = models.CharField(max_length=250, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.OneToOneField(
        Image,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

from django.db import models

# Create your models here.


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


class Image(models.Model):
    path = models.FilePathField(path="/projects/static/img")
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
    description = models.CharField(max_length=2000)
    source_url = models.CharField(max_length=250, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

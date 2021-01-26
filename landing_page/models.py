from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from solo.models import SingletonModel
# Create your models here.


class Work(models.Model):
    job_title = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    present = models.BooleanField()
    company = models.CharField(max_length=120)
    short_description = models.CharField(max_length=150)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ['start_date']
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experience"


class Education(models.Model):
    field_of_study = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    present = models.BooleanField()
    institution = models.CharField(max_length=120)
    short_description = models.CharField(max_length=150)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.field_of_study

    class Meta:
        ordering = ['start_date']
        verbose_name = "Education"
        verbose_name_plural = "Education"


class Skill(models.Model):
    name = models.CharField(max_length=120)
    percentage = models.IntegerField(
        default=60,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SiteConfiguration(SingletonModel):
    name = models.CharField(max_length=120)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254)
    welcome_message = models.CharField(max_length=255)
    hobbies_text = RichTextField()
    avatar_url = models.URLField(default="http://placekitten.com/g/200/300")
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"


# Generated by Django 3.1.3 on 2020-12-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.FilePathField(path='/static/projects/img'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
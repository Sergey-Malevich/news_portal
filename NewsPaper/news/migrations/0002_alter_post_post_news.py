# Generated by Django 5.0.3 on 2024-04-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_news',
            field=models.CharField(choices=[('POST', 'Статья'), ('NEWS', 'Новость')], default='POST', max_length=20),
        ),
    ]
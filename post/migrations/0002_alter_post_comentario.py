# Generated by Django 5.0 on 2023-12-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comentario',
            field=models.ManyToManyField(blank=True, null=True, to='post.comentario'),
        ),
    ]
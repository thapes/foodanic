# Generated by Django 3.1.7 on 2021-06-23 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prep', models.CharField(max_length=255)),
                ('cook', models.CharField(max_length=255)),
                ('servings', models.IntegerField(blank=True, default=1, null=True)),
                ('image', models.ImageField(upload_to='media/')),
                ('ingredients', markdownx.models.MarkdownxField()),
                ('directions', markdownx.models.MarkdownxField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

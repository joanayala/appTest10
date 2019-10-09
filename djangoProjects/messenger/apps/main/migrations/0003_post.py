# Generated by Django 2.2.4 on 2019-10-07 14:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Create date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(max_length=200, upload_to='images/', verbose_name='Image')),
                ('published', models.BooleanField(default=False, verbose_name='Published / No published')),
                ('published_date', models.DateField(verbose_name='Published date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]

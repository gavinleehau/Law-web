# Generated by Django 3.2.7 on 2021-12-20 04:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', verbose_name='Tiêu đề')),
                ('content', ckeditor.fields.RichTextField(verbose_name='nội dung')),
            ],
            options={
                'db_table': 'services',
                'ordering': ['-id'],
            },
        ),
    ]
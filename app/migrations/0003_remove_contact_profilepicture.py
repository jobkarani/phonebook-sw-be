# Generated by Django 4.1.2 on 2023-03-02 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contact_remove_blogs_blog_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='profilePicture',
        ),
    ]

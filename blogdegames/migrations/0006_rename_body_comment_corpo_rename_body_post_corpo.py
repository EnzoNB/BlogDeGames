# Generated by Django 4.2.7 on 2023-11-21 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogdegames', '0005_rename_author_post_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='corpo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='corpo',
        ),
    ]

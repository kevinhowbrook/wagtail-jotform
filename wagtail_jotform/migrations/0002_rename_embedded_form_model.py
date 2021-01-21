# Generated by Django 3.1.1 on 2020-10-09 08:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0052_pagelogentry'),
        ('wagtail_jotform', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmbededFormPage',
            new_name='EmbeddedFormPage',
        ),
    ]

# Generated by Django 2.2.7 on 2020-01-13 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_page_meta', '0011_auto_20190218_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagemeta',
            name='gplus_author',
        ),
        migrations.RemoveField(
            model_name='pagemeta',
            name='gplus_type',
        ),
        migrations.RemoveField(
            model_name='titlemeta',
            name='gplus_description',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-14 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repo',
            old_name='lanuage',
            new_name='language',
        ),
    ]
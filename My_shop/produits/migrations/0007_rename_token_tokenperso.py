# Generated by Django 5.0.3 on 2024-04-03 16:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0006_token'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Token',
            new_name='TokenPerso',
        ),
    ]

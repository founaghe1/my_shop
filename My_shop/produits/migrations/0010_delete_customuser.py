# Generated by Django 5.0.3 on 2024-04-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0009_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
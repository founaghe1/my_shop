# Generated by Django 5.0.3 on 2024-04-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
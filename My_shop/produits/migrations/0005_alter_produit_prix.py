# Generated by Django 5.0.3 on 2024-04-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0004_alter_produit_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]

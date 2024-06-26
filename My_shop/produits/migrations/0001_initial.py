# Generated by Django 5.0.3 on 2024-03-29 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite', models.IntegerField()),
                ('description', models.TextField()),
                ('category_modif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produits.categories')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discountedprice',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
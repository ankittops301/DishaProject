# Generated by Django 4.0.4 on 2022-06-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=50)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('pic', models.FileField(default='avtar.png', upload_to='seller profile')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
                ('brand', models.CharField(max_length=32)),
                ('model', models.CharField(max_length=32)),
                ('condition', models.CharField(max_length=32)),
                ('isRented', models.BooleanField(default=False)),
            ],
        ),
    ]
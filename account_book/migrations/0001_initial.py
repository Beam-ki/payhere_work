# Generated by Django 4.1.5 on 2023-01-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=None)),
                ('memo', models.CharField(blank=None, max_length=9999)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cne', models.CharField(max_length=20)),
                ('cin', models.CharField(max_length=20)),
            ],
        ),
    ]

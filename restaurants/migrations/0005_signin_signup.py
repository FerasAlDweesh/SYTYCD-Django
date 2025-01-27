# Generated by Django 2.2.6 on 2019-10-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20180419_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=105)),
                ('password', models.CharField(max_length=105)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=105)),
                ('first_name', models.CharField(max_length=105)),
                ('last_name', models.CharField(max_length=105)),
                ('email', models.CharField(max_length=105)),
                ('password', models.CharField(max_length=105)),
            ],
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-16 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('user_pwd', models.CharField(max_length=64)),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aalu', '0003_alter_signin_email_alter_signin_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('movie', models.CharField(max_length=100)),
            ],
        ),
    ]
# Generated by Django 5.0.1 on 2024-06-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aalu', '0002_login_review1_signin_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='signin',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral_system', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

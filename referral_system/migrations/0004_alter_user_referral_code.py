# Generated by Django 5.0.4 on 2024-04-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral_system', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
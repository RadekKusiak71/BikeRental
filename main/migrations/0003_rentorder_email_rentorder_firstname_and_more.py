# Generated by Django 4.2.1 on 2023-06-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rentorder_session_key_alter_rentorder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentorder',
            name='email',
            field=models.EmailField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='rentorder',
            name='firstname',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='rentorder',
            name='lastname',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
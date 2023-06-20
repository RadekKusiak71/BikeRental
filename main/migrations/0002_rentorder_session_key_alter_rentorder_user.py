# Generated by Django 4.2.1 on 2023-06-20 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentorder',
            name='session_key',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rentorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.userprofile'),
        ),
    ]

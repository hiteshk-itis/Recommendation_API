# Generated by Django 4.0.4 on 2023-10-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessingComponent', '0003_alter_userlistpreprocessed_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlistpreprocessed',
            name='register_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistpreprocessed',
            name='updated_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistraw',
            name='register_datetime',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistraw',
            name='updated_datetime',
            field=models.TextField(blank=True, null=True),
        ),
    ]

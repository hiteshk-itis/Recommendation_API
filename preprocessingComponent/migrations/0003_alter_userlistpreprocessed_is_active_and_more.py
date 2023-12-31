# Generated by Django 4.0.4 on 2023-10-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessingComponent', '0002_alter_courseratingpreprocessed_course_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlistpreprocessed',
            name='is_active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistpreprocessed',
            name='is_center_admin',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistpreprocessed',
            name='is_student',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistpreprocessed',
            name='is_teacher',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistpreprocessed',
            name='member_department',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistpreprocessed',
            name='use_flag',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistraw',
            name='register_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlistraw',
            name='updated_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

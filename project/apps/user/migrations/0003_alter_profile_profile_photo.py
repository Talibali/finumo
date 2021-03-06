# Generated by Django 3.2.5 on 2021-07-27 06:30

from django.db import migrations, models
import project.core.storage


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.FileField(blank=True, null=True, upload_to=project.core.storage.profile_photo_path),
        ),
    ]

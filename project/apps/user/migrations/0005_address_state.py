# Generated by Django 3.2.5 on 2021-07-27 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('user', '0004_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='common.state'),
        ),
    ]
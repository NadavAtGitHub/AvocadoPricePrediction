# Generated by Django 3.0.8 on 2020-07-23 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_prediction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avocadoorder',
            old_name='exra_large_bags',
            new_name='extra_large_bags',
        ),
        migrations.RemoveField(
            model_name='avocadoorder',
            name='medium_bags',
        ),
    ]
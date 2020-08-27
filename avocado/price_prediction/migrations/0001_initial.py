# Generated by Django 3.0.8 on 2020-07-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvocadoOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_volume', models.DecimalField(decimal_places=5, max_digits=20)),
                ('num_plu_4046', models.DecimalField(decimal_places=5, max_digits=20)),
                ('num_plu_4225', models.DecimalField(decimal_places=5, max_digits=20)),
                ('total_bags', models.DecimalField(decimal_places=5, max_digits=20)),
                ('num_plu_4770', models.DecimalField(decimal_places=5, max_digits=20)),
                ('small_bags', models.DecimalField(decimal_places=5, max_digits=20)),
                ('medium_bags', models.DecimalField(decimal_places=5, max_digits=20)),
                ('large_bags', models.DecimalField(decimal_places=5, max_digits=20)),
                ('extra_large_bags', models.DecimalField(decimal_places=5, max_digits=20)),
                ('avocado_type', models.CharField(choices=[('conventional', 'conventional'), ('organic', 'organic')],
                                                  max_length=50)),
                ('region', models.CharField(choices=[('Albany', 'Albany')], max_length=50)),
                ('year', models.IntegerField()),
            ],
        ),
    ]

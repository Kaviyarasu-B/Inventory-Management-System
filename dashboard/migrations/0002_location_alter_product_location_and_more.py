# Generated by Django 4.2.2 on 2023-08-13 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.location'),
        ),
        migrations.AlterField(
            model_name='productmovement',
            name='from_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_movements', to='dashboard.location'),
        ),
        migrations.AlterField(
            model_name='productmovement',
            name='to_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_movements', to='dashboard.location'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-01 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='LittleLemonAPI.order'),
        ),
    ]
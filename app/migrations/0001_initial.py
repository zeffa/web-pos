# Generated by Django 3.0.4 on 2020-03-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=200)),
                ('product_type', models.CharField(max_length=200)),
                ('product_manufacturer', models.CharField(max_length=200)),
                ('product_category', models.CharField(max_length=200)),
                ('product_distributor', models.CharField(max_length=200)),
                ('wholesale_price', models.CharField(max_length=50)),
                ('retail_price', models.CharField(max_length=200)),
                ('vat', models.CharField(max_length=200)),
                ('product_code', models.CharField(max_length=200)),
                ('sync_status', models.SmallIntegerField(default=1)),
                ('delete_status', models.SmallIntegerField(default=1)),
                ('depot_id', models.IntegerField()),
            ],
        ),
    ]
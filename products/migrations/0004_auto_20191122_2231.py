# Generated by Django 2.2.4 on 2019-11-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191122_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]
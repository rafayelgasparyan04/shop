# Generated by Django 2.2.4 on 2019-11-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='productpic/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='products.categories'),
        ),
    ]

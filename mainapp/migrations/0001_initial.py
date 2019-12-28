# Generated by Django 2.2.4 on 2019-11-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50)),
                ('send_title', models.CharField(max_length=50)),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('sender_phone', models.CharField(blank=True, max_length=15)),
                ('sender_email', models.EmailField(max_length=254)),
                ('send_text', models.TextField(max_length=800)),
            ],
        ),
    ]
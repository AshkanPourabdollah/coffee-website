# Generated by Django 4.2.4 on 2023-09-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='coffeeName',
            field=models.CharField(default='', max_length=50),
        ),
    ]

# Generated by Django 3.2 on 2022-03-27 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_dessert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

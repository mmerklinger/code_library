# Generated by Django 2.2.1 on 2019-05-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20190526_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]

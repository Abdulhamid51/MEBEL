# Generated by Django 3.2.4 on 2021-09-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False, verbose_name='aktiv / noaktiv '),
        ),
    ]
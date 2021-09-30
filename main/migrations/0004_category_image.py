# Generated by Django 3.2.5 on 2021-09-29 18:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='category_images/', verbose_name='image'),
            preserve_default=False,
        ),
    ]
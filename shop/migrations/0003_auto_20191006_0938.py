# Generated by Django 2.2.5 on 2019-10-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190929_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
# Generated by Django 4.0 on 2021-12-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='format: required, max-100', max_length=100, verbose_name='category name'),
        ),
    ]
# Generated by Django 3.1.6 on 2022-09-09 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0002_auto_20220909_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ('id',), 'verbose_name': 'Offer', 'verbose_name_plural': 'Offers'},
        ),
    ]

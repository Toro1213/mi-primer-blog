# Generated by Django 3.2.25 on 2025-06-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rugby', '0003_jugadorrugby_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadorrugby',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
    ]

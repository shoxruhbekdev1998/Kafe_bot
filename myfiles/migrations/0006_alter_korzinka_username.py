# Generated by Django 4.2 on 2023-05-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_korzinka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korzinka',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
# Generated by Django 2.1 on 2018-09-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sold', '0003_auto_20180929_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solddata',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solddata',
            name='zipCode',
            field=models.CharField(max_length=200),
        ),
    ]
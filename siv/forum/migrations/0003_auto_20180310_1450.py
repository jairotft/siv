# Generated by Django 2.0 on 2018-03-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20180310_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationpreference',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='messagerecord',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='opinionmessage',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraction',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='worrycategory',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='worrymessage',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='worrytype',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='worryuser',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
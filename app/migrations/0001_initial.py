# Generated by Django 3.1.5 on 2021-01-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=200, verbose_name='hash')),
                ('height', models.IntegerField(default=0, verbose_name='height')),
                ('timestamp', models.IntegerField(default=0, verbose_name='timestamp')),
                ('transactionCount', models.IntegerField(default=0, verbose_name='transactionCount')),
                ('miner', models.CharField(max_length=200, verbose_name='miner')),
            ],
            options={
                'verbose_name': 'Blocks',
            },
        ),
    ]

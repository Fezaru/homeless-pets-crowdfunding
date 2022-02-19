# Generated by Django 4.0.1 on 2022-02-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='external_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='fur_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='height',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='litter_box_trained',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='original_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

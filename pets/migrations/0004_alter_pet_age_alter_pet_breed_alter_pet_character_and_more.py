# Generated by Django 4.0.1 on 2022-02-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_alter_pet_age_alter_pet_breed_alter_pet_character_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.CharField(max_length=255, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Порода'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='character',
            field=models.CharField(max_length=255, verbose_name='Характер'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='curator_info',
            field=models.CharField(max_length=255, verbose_name='Информация о кураторе'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='feeding',
            field=models.CharField(max_length=255, verbose_name='Кормление'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='flea_treatment',
            field=models.CharField(max_length=255, verbose_name='Обработка от клещей/блох'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='fur_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип шерсти'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='height',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Высота в холке'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='in_catalog_since',
            field=models.CharField(max_length=255, verbose_name='В каталоге с'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='litter_box_trained',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Приучен(а) к лотку'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(blank=True, choices=[('cat', 'Кот'), ('dog', 'Собака'), ('kitten', 'Котенок'), ('puppy', 'Щенок')], max_length=255, null=True, verbose_name='Тип животного'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=255, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='shelter',
            field=models.CharField(max_length=255, verbose_name='Приют'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='vet_peculiarities',
            field=models.CharField(max_length=255, verbose_name='Ветеринарные особенности(стерилизована, кастрирован и т.п.)'),
        ),
    ]

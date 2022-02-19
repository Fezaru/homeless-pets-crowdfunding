from django.conf import settings
from django.db import models
from django.urls import reverse


def upload_gallery_image(instance, filename):
    return f"images/{instance.pet.external_id}/gallery/{filename}.jpg"


class BaseModel(models.Model):
    class Meta:
        abstract = True


class Pet(BaseModel):
    GIRL = 'Девочка'
    BOY = 'Мальчик'
    # pet types
    CAT = 'cat'
    DOG = 'dog'
    KITTEN = 'kitten'
    PUPPY = 'puppy'
    SEX_CHOICES = [
        (BOY, BOY),
        (GIRL, GIRL),
    ]

    PET_TYPE_CHOICES = [
        (CAT, 'Кот'),
        (DOG, 'Собака'),
        (KITTEN, 'Котенок'),
        (PUPPY, 'Щенок'),
    ]
    # custom
    original_url = models.URLField(null=True, blank=True)
    external_id = models.CharField(max_length=255, null=True, blank=True)
    created_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    # general
    pet_type = models.CharField('Тип животного', max_length=255, null=True, blank=True, choices=PET_TYPE_CHOICES)
    name = models.CharField('Имя', max_length=255, )
    description = models.CharField('Описание', max_length=255, )
    sex = models.CharField('Пол', max_length=255, choices=SEX_CHOICES)
    age = models.CharField('Возраст', max_length=255, )
    vet_peculiarities = models.CharField('Ветеринарные особенности(стерилизована, кастрирован и т.п.)', max_length=255, )
    flea_treatment = models.CharField('Обработка от клещей/блох', max_length=255, )
    fur_type = models.CharField('Тип шерсти', max_length=255, null=True, blank=True)
    character = models.CharField('Характер', max_length=255, )
    feeding = models.CharField('Кормление', max_length=255, )
    litter_box_trained = models.CharField('Приучен(а) к лотку', max_length=255, null=True, blank=True)
    in_catalog_since = models.CharField('В каталоге с', max_length=255, )
    shelter = models.CharField('Приют', max_length=255, )
    curator_info = models.CharField('Информация о кураторе', max_length=255, )
    # for dogs
    height = models.CharField('Высота в холке', max_length=255, null=True, blank=True)
    breed = models.CharField('Порода', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pets-detail', kwargs={'pk': self.pk})


class Image(BaseModel):
    image = models.ImageField(upload_to=upload_gallery_image)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='images')

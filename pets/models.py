from django.db import models
from django.conf import settings


def upload_gallery_image(instance, filename):
    return f"images/{instance.pet.external_id}/gallery/{filename}.jpg"


class BaseModel(models.Model):
    class Meta:
        abstract = True


class Pet(BaseModel):
    GIRL = 'Девочка'
    BOY = 'Мальчик'
    SEX_CHOICES = [
        (BOY, BOY),
        (GIRL, GIRL),
    ]
    # custom
    original_url = models.URLField()
    pet_type = models.TextField(null=True, blank=True)
    external_id = models.TextField()
    created_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    # general
    name = models.TextField()
    description = models.TextField()
    sex = models.TextField(choices=SEX_CHOICES)
    age = models.TextField()
    vet_peculiarities = models.TextField()
    flea_treatment = models.TextField()
    fur_type = models.TextField()
    character = models.TextField()
    feeding = models.TextField()
    litter_box_trained = models.TextField()
    in_catalog_since = models.TextField()
    shelter = models.TextField()
    curator_info = models.TextField()
    # for dogs
    height = models.TextField()
    breed = models.TextField()


class Image(BaseModel):
    image = models.ImageField(upload_to=upload_gallery_image)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='images')

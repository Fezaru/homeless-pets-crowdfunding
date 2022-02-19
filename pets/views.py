from datetime import date

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from pets.models import Pet, Image


class PetsCatalogListView(ListView):
    model = Pet
    template_name = 'pets/pets_catalog_list.html'
    context_object_name = 'pets'
    paginate_by = 30


class PetsCatalogDetailView(DetailView):
    model = Pet
    template_name = 'pets/pets_catalog_detail.html'
    context_object_name = 'pet'


class PetsCatalogCreateView(CreateView):
    template_name = 'pets/pets_catalog_form.html'
    model = Pet
    fields = ['pet_type', 'name', 'description', 'sex', 'age', 'vet_peculiarities', 'flea_treatment', 'character',
              'feeding', 'shelter', 'curator_info', 'fur_type', 'height', 'breed', 'litter_box_trained']

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user
        form.instance.in_catalog_since = f'С {date.today()}'
        self.object = form.save()
        for image in self.request.FILES.getlist('uploaded_images'):
            Image.objects.create(pet=self.object, image=image)
        return super().form_valid(form)

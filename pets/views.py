from django.views.generic import (
    ListView,
    DetailView)

from pets.models import Pet


class PetsCatalogListView(ListView):
    model = Pet
    template_name = 'pets/pets_catalog_list.html'
    context_object_name = 'pets'
    paginate_by = 30


class PetsCatalogDetailView(DetailView):
    model = Pet
    template_name = 'pets/pets_catalog_detail.html'
    context_object_name = 'pet'

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import date

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
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


class PetsCatalogCreateView(LoginRequiredMixin, CreateView):
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


class PetsCatalogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'pets/pets_catalog_form.html'
    model = Pet
    fields = ['pet_type', 'name', 'description', 'sex', 'age', 'vet_peculiarities', 'flea_treatment', 'character',
              'feeding', 'shelter', 'curator_info', 'fur_type', 'height', 'breed', 'litter_box_trained']

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user
        if self.request.FILES.getlist('uploaded_images'):
            self.object = form.save()
            self.object.images.all().delete()
            for image in self.request.FILES.getlist('uploaded_images'):
                Image.objects.create(pet=self.object, image=image)
        return super().form_valid(form)

    def test_func(self):
        pet = self.get_object()
        if self.request.user == pet.created_by_user:
            return True
        return False


class PetsCatalogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'pets/pets_catalog_confirm_delete.html'
    model = Pet
    success_url = '/pets'

    def test_func(self):
        pet = self.get_object()
        if self.request.user == pet.created_by_user:
            return True
        return False

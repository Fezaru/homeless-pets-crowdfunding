from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from pets.models import Pet, Image
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)


class PetsCatalogListView(ListView):
    template_name = 'pets/pets_catalog_list.html'
    context_object_name = 'pets'
    model = Pet
    paginate_by = 30

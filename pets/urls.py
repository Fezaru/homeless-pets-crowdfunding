from django.urls import path
from pets import views

urlpatterns = [
    path('', views.PetsCatalogListView.as_view(), name='pets-home'),
    path('pets/', views.PetsCatalogListView.as_view(), name='pets-home'),
    path('pets/<int:pk>/', views.PetsCatalogDetailView.as_view(), name='pets-detail'),

]

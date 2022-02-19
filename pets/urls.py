from django.urls import path
from pets import views

urlpatterns = [
    path('', views.PetsCatalogListView.as_view(), name='pets-home'),
    path('pets/', views.PetsCatalogListView.as_view(), name='pets-home'),
    path('pets/<int:pk>/', views.PetsCatalogDetailView.as_view(), name='pets-detail'),
    path('pets/new/', views.PetsCatalogCreateView.as_view(), name='pets-create'),
    path('pets/<int:pk>/update/', views.PetsCatalogUpdateView.as_view(), name='pets-update'),
    path('pets/<int:pk>/delete/', views.PetsCatalogDeleteView.as_view(), name='pets-delete'),

]

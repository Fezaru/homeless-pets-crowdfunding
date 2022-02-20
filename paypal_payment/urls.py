from django.urls import path, include
from paypal_payment import views

urlpatterns = [
    path('process/', views.payment_process, name='payment-process'),
    path('done/', views.payment_done, name='payment-done'),
    path('cancelled/', views.payment_cancelled, name='payment-cancelled'),
]

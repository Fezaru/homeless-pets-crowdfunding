from uuid import uuid4

from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm


@csrf_exempt
def payment_done(request):
    return render(request, 'paypal_payment/done.html')


@csrf_exempt
def payment_cancelled(request):
    return render(request, 'paypal_payment/cancelled.html')


def payment_process(request):
    payment_id = uuid4()
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': None,
        'item_name': f'Donation {payment_id}',
        'invoice': str(payment_id),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("payment-done")}',
        'cancer_url': f'http://{host}{reverse("payment-cancelled")}',
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal_payment/process.html', {'form': form})

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Handle the delivery logic
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.DELIVERY_OPTION_THRESHOLD:
        delivery = 0
        delivery_available_delta = settings.DELIVERY_OPTION_THRESHOLD - total
    else:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        delivery_available_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'delivery_available_delta': delivery_available_delta,
        'delivery_option_threshold': settings.DELIVERY_OPTION_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    """
    Handle the delivery logic
    """

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.DELIVERY_OPTION_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        delivery_available_delta = settings.DELIVERY_OPTION_THRESHOLD - total
    else:
        delivery = 0
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

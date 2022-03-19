from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category

# Create your views here.


def all_products(request):
    """A view to show products, proced searchs and sorting """

    products = Product.objects.all()
    query = None
    categories = None
    sweet_sauvory_query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

            # Second query to lookout to Sweet or Savoury field
            if 'sweet_sauvory' in request.GET:
                sweet_sauvory_query = request.GET['sweet_sauvory']
                products = products.filter(
                    sweet_sauvory=sweet_sauvory_query)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You did not enter any info search criteria")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'sweet_sauvory ': sweet_sauvory_query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view individual product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

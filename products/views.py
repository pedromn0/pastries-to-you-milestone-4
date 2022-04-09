from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """A view to show products, proced searchs and sorting """

    products = Product.objects.all()
    query = None
    categories = None
    sweet_sauvory_query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'sweet_sauvory ': sweet_sauvory_query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view individual product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure that all data was filled correctly.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit product from the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update the product. Please ensure that all data was filled correctly.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

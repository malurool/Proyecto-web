from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from shop.models import Product, Category
from cart.forms import QuantityForm

from .forms import ContactForm


def paginat(request, list_objects):
	p = Paginator(list_objects, 20)
	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number)
	except PageNotAnInteger:
		page_obj = p.page(1)
	except EmptyPage:
		page_obj = p.page(p.num_pages)
	return page_obj


def home_page(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'home_page.html', context)


def product_detail(request, slug):
    form = QuantityForm()
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).all()[:5]

    context = {
        'title': product.title,
        'product': product,
        'form': form,
        'favorites': 'favorites',
        'related_products': related_products,
    }

    if request.user.is_authenticated:
        if request.user.likes.filter(id=product.id).exists():
            context['favorites'] = 'remove'
    else:
        messages.warning(request, "Debes iniciar sesión para agregar productos a favoritos o realizar una compra.")

    return render(request, 'product_detail.html', context)

@login_required
def add_to_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.add(product)
	return redirect('shop:product_detail', slug=product.slug)


@login_required
def remove_from_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.remove(product)
	return redirect('shop:favorites')


@login_required
def favorites(request):
	products = request.user.likes.all()
	context = {'title':'Favoritos', 'products':products}
	return render(request, 'favorites.html', context)


def search(request):
	query = request.GET.get('q')
	products = Product.objects.filter(title__icontains=query).all()
	context = {'products': paginat(request ,products)}
	return render(request, 'home_page.html', context)


def filter_by_category(request, slug):

	result = []
	category = Category.objects.filter(slug=slug).first()
	[result.append(product) \
		for product in Product.objects.filter(category=category.id).all()]
	# check if category is parent then get all sub-categories
	if not category.is_sub:
		sub_categories = category.sub_categories.all()
		# get all sub-categories products 
		for category in sub_categories:
			[result.append(product) \
				for product in Product.objects.filter(category=category).all()]
	context = {'products': paginat(request ,result)}
	return render(request, 'home_page.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # guarda el mensaje en la base de datos
            messages.success(request, 'Tu mensaje fue enviado correctamente 💌')
            return redirect('shop:contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
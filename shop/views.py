from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand
from django.views import View
from cart.forms import CartAddProductForm
from .documents import ProductsDocument
from .parsing import habr_link1, habr_img1, habr_text1, habr_link2, habr_img2, habr_text2, habr_link3, habr_img3, habr_text3


def brands_views(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(available=True)
    products = products.filter(brand=brand)
    brands = Brand.objects.all()
    categories = Category.objects.all()

    context = {
        'brand': brand,
        'products': products,
        'brands': brands,
        'categories': categories,
    }
    return render(request, 'shop/brand.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()
    brands = Brand.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'categories': categories,
        'product': product,
        'cart_product_form': cart_product_form,
        'brands': brands,
    }
    return render(request, 'shop/product/detail.html', context)


def product_list(request, category_slug=None):
    habr_l1 = habr_link1()
    habr_i1 = habr_img1()
    habr_t1 = habr_text1()
    habr_l2 = habr_link2()
    habr_i2 = habr_img2()
    habr_t2 = habr_text2()
    habr_l3 = habr_link3()
    habr_i3 = habr_img3()
    habr_t3 = habr_text3()
    category = None
    brands = Brand.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'brands': brands,
        'habr_l1': habr_l1,
        'habr_i1': habr_i1,
        'habr_t1': habr_t1,
        'habr_l2': habr_l2,
        'habr_i2': habr_i2,
        'habr_t2': habr_t2,
        'habr_l3': habr_l3,
        'habr_i3': habr_i3,
        'habr_t3': habr_t3
    }
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        context = {
            'category': category,
            'categories': categories,
            'products': products
        }
        return render(request, 'shop/product/list.html', context)
    return render(request, 'shop/base.html', context)


class ElasticSearchView(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        search_result = ProductsDocument.search().query('match', category__name=query)
        if not search_result:
            search_result = ''
        return render(request, 'shop/search.html', {'search_result': search_result})

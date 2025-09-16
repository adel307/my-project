from django.shortcuts import render
from pages.models import Product, Clint, Market

def product_list(request):
    """
    عرض قائمة جميع المنتجات، العملاء، والأسواق
    """

    # جلب جميع البيانات مع تحسين الأداء
    products = Product.objects.all()
    clints = Clint.objects.all().select_related()
    markets = Market.objects.all().prefetch_related('vesetors', 'market_products')
    
    context = {
        'products_num': str(products.count()),
        'product_card': products.select_related('product_time'),
        'clints_card': clints,
        'markets_card': markets
    }
    
    return render(request, 'products/products.html', context)
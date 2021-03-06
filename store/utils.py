from .models  import Product


def filter_min_max(request, products):
    min_price = request.GET.get("min", None)
    max_price =  request.GET.get("max",None)
    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price) 
    
    return products 


def condition_filter(request):
    holat = request.GET.get('holat',None)
    if holat:
        products = Product.objects.filter(condition=holat)
        products = filter_min_max(request, products)
    else:
        products = Product.objects.all()
        products = filter_min_max(request, products) 

    return products



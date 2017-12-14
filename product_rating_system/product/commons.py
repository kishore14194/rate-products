from product.models import ProductDetail, ProductRating


def get_pro_obj(pro_id):
    """Check if product exists"""
    try:
        pro_obj = ProductDetail.objects.get(product_id=pro_id)
    except ProductDetail.DoesNotExist:
        return None
    return pro_obj


def rating_avg(product_obj):
    rating_list = ProductRating.objects.filter(product=product_obj).values_list('rating', flat=True)
    if rating_list:
        avg_rating = sum(rating_list)/len(rating_list)
        return avg_rating

    return None

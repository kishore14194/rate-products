from .models import ProductDetail


def format_product(data):
    """ Format product values to store in the database"""
    product_name = data.get('product_name')
    pro_details = {
        "product_id": generate_pro_id(product_name),
        "product_name": product_name,
        "mrp": data.get('mrp', 0),
        "product_desc": data.get('product_desc', ''),
        "status": True
    }

    return pro_details


def generate_pro_id(product_name):
    """Generate product id for newly added product"""

    pro_id = ProductDetail.objects.latest('id')
    pro_id = str(pro_id.id+1)
    pro_val = product_name[:3] + pro_id

    return pro_val


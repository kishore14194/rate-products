from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view_all/$', views.ProductList.as_view(), name='view_all'),
    url(r'^add/$', views.ProductAdd.as_view(), name='add'),
    # url(r'^inactive/$', views.InventoryNotActive.as_view(), name='inactive'),
    # url(r'^approve/$', views.InventoryApprove.as_view(), name='approve'),
    url(r'^remove/$', views.DeleteProduct.as_view(), name='remove'),
]
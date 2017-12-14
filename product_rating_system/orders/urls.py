from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.CreateOrder.as_view(), name='view_all'),
    # url(r'^add/$', views.ProductAdd.as_view(), name='add'),
    # url(r'^remove/$', views.DeleteProduct.as_view(), name='remove'),
    # url(r'^rate/$', views.RateProduct.as_view(), name='remove'),
]
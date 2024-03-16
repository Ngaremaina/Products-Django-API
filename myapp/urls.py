from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductView.as_view(), name = 'products'),
    path('products/<int:pk>', ProductViewDetails.as_view(), name = 'product'),
    path('variants/', ProductVariantView.as_view(), name = 'variants'),
    path('variants/<int:pk>', ProductVariantViewDetails.as_view(), name = 'variant'),

    
]
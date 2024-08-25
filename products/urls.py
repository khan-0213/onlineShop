from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView, user_profile
)

urlpatterns = [
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('', ProductListView.as_view(), name='product_list'),
    path('new/', ProductCreateView.as_view(), name='product_new'),
    path('profile/', user_profile, name='user_profile'),
]
from django.urls import path
from shop.views import ElasticSearchView
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('elasticsearch_results/', ElasticSearchView.as_view(), name='elasticsearch'),
    path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<str:brand_slug>', views.brands_views, name='brands_views'),
    path('<str:id>/<str:slug>/', views.product_detail, name='product_detail'),

]
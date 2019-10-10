from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('shop:product_list')), name='logout'),
    path('registration/', views.registration_view, name='registration'),
    path('edit/', views.edit_view, name='edit'),
    path('account/', views.account_view, name='account'),
]

from django.urls import path
from .views.accounts import *
from .views.main import *

urlpatterns = [
    path("accounts/profiles/", ProfileApiView.as_view(), name="profiles"),
    #product urls
    path("products/", ProductApiView.as_view({'get':'list'}), name="products"),
    path("products/<pk>", ProductApiView.as_view({'get':'retrieve'}), name="product_detail"),
    path("products/<int:product_id>/reviews/", ReviewApiView.as_view(), name="reviews"),
    path("products/review/create/", ReviewCreateApiView.as_view(), name="review_create"),

    path("uid/", LoginApiView.as_view(), name="uid"),
    path("register/", RegisterApiView.as_view(), name="register")
]

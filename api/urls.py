from django.urls import path
from .views.accounts import *
from .views.main import *

urlpatterns = [
    path("accounts/profiles/", ProfileApiView.as_view(), name="profiles"),
    path("products/", ProductApiView.as_view(), name="products"),
]

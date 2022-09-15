from django.urls import path
from .views.accounts import *

urlpatterns = [
    path("accounts/profiles/", ProfileApiView.as_view(), name="profiles"),
]

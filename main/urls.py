from django.urls import path
from.import views

app_name = 'main'

urlpatterns = [
    path('',views.HomeView.as_view(), name='Home'),
    path("about/", views.AboutView.as_view(), name="about"),
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("catalog/", views.CatalogView.as_view(), name="catalog"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("sigin/", views.RegisterctView.as_view(), name="sigin"),
    path("contact/", views.contact, name="contact"),
    path("wishlist/", views.WishlistView.as_view(), name="wishlist"),
<<<<<<< HEAD
    path('search/', views.search, name='search'),
=======
    path("product/<link>", views.detail_product, name="detail_product")
>>>>>>> d1c71b95d6d9bb04390e0168f8bfa7a0597a564a
]

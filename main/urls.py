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
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("wishlist/", views.WishlistView.as_view(), name="wishlist"),
]

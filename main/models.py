from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField("nomi", max_length=150)
    slug = models.models.SlugField("slug")

    def __str__(self):
        return self.title

class Images(models.Model):
    img = models.ImageField("rasmi", upload_to='product_images/')

class Product(models.Model):
    title = models.CharField("title", max_length=150)
    owner = models.ForeignKey("accounts.ClientUser", related_name="products", on_delete=models.CASCADE)
    link = models.CharField("link", max_length=50, unique=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    content = models.TextField("tarif")
    images = models.ManyToManyField(Images, related_name="product")
    price = models.PositiveIntegerField("narxi", default=0)
    old_price = models.PositiveIntegerField("eski narxi", default=0)
    for_slider = models.BooleanField("birinchiga")
    for_duel = models.BooleanField("ikkitalikga")
    for_big = models.BooleanField("kattaga")

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    user = models.ForeignKey("accounts.UserProfile", related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField("comment")

    def __str__(self):
        return self.user
    
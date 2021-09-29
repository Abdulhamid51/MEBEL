from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField("nomi", max_length=150)
    image = models.ImageField('image', upload_to='category_images/')
    slug = models.SlugField("slug")

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
    img1 = models.ImageField("rasmi1", upload_to='product_images/',blank=True,null=True)
    img2 = models.ImageField("rasmi2", upload_to='product_images/',blank=True,null=True)
    img3 = models.ImageField("rasmi3", upload_to='product_images/',blank=True,null=True)
    img4 = models.ImageField("rasmi4", upload_to='product_images/',blank=True,null=True)
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


class Banner(models.Model):
    image = models.ImageField("Banner rasmi", upload_to='banner/', height_field=None, width_field=None, max_length=None)
    title = models.TextField("Banner matni")


class Contact(models.Model):
    name = models.CharField("F,I,SH",max_length=250)
    email = models.EmailField('Elektron pochta',max_length=100,blank=True,null=True)
    subject = models.CharField("Mavzu", max_length=50,blank=True,null=True)
    phone = models.CharField("Telfon raqami",max_length=20)
    message = models.TextField("Xabari")

    class Meta:
        verbose_name = "Aloqa"
        verbose_name_plural = "Aloqalar"
    def __str__ (self):
        return f'{self.name}'


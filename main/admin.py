from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(MaterialTypes)
admin.site.register(Reviews)
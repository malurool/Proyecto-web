from django.contrib import admin

from .models import Category, Product
from .models import ContactMessage 

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ContactMessage)

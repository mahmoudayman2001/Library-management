from django.contrib import admin
from .models import BooK
from .models import Category

# Register your models here.
admin.site.register(BooK)
admin.site.register(Category)
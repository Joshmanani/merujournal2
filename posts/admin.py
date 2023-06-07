from django.contrib import admin

# Register your models here.
from .models import Post, Category, Volume, Journal

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Volume)
admin.site.register(Journal)
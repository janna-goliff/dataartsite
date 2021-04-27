from django.contrib import admin
from mainproject.models import Picture, FilteredPicture

# Register your models here.
admin.site.register(Picture)
admin.site.register(FilteredPicture)
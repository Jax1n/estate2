from django.contrib import admin
from . models import *

class ImageInline(admin.TabularInline):
    model = Image
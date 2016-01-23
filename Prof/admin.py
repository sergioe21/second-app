from django.contrib import admin

# Register your models here.
from .models import Worker, Counter

admin.site.register(Worker)

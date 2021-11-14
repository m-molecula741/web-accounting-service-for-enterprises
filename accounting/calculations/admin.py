from django.contrib import admin
from .models import AccInfo, Income, Expenses

admin.site.register(AccInfo)
admin.site.register(Income)
admin.site.register(Expenses)
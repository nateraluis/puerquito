from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Currency)
admin.site.register(CategoryIncome)
admin.site.register(CategoryExpense)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Household)

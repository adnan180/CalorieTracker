from django.contrib import admin
from .models import Food, Consume

# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ["name", "carbs", "protein", "fats", "calories"]


class ConsumeAdmin(admin.ModelAdmin):
    list_display = ["user", "foodconsumed"]


admin.site.register(Food, FoodAdmin)
admin.site.register(Consume, ConsumeAdmin)

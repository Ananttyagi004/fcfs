from django.contrib import admin
from .models import UserProfile, Category, Transaction

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'phone', 'address')
    list_filter = ('user',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('user',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'category', 'description')
    search_fields = ('user__username', 'category__name', 'description')
    list_filter = ('date', 'category')

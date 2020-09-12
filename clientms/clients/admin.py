from django.contrib import admin

from .models import Client, Comment, Vehicle


class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number']


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = ['client', 'make', 'model', 'VIN', 'DatePurchase', 'LastService']


admin.site.register(Client, ClientAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Comment)

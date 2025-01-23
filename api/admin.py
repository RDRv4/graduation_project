from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from api.models.client_models import Client
from api.models.product_models import Product


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ("first_name", "surname", "store", "phone_number")
	list_filter = (('birth_day', DateRangeFilter), "store", "short_description",)
	search_fields = ("store", "short_description",)

	save_on_top = True
	save_as = True

	fieldsets = (
		("Client", {
			"fields": (("first_name", "surname", "birth_day",),)
		}),
		("Description", {
			"fields": (("short_description", "store"),)
		}),
		("Contacts", {
			"fields": (("phone_number", "email",),)
		}),
	)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ("name", "brand", "image_url",)
	list_filter = ("brand", "price", "size", "fatness")
	search_fields = ("brand", "name",)

	save_on_top = True
	save_as = True

	fieldsets = (
        ("Brand", {
			"fields": (("brand",),)
		}),
		("Description", {
			"fields": (("name", "description", "image_url"),)
		}),
		("Opional", {
			"fields": (("size", "fatness", "price", "good_url"),)
		}),
	)


admin.site.site_title = "Managment system"
admin.site.site_header = "Managment system"

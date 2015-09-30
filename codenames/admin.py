from django.contrib import admin

# Register your models here.
from .models import Agency, Location, Prefix, Operation

class AgencyAdmin(admin.ModelAdmin):
	fields=['name']
	search_fields=['name']

class LocationAdmin(admin.ModelAdmin):
	fields=['country', 'longitude', 'latitude']
	list_filter=['country']

class PrefixAdmin(admin.ModelAdmin):
	fields=['prefix', 'agency']

class OperationAdmin(admin.ModelAdmin):
	fieldsets=[
		(None, {'fields':['prefix', 'code_word']}),
		('Operation Information', {'fields':['op_num','clearance','location', 'start_date', 'end_date', 'active']}),
		('Administration Information', {'fields': ['agency', 'user']}),
	]
	search_fields=['prefix','code_word','op_num']
	list_filter=['agency', 'prefix', 'active']

admin.site.register(Agency, AgencyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Prefix, PrefixAdmin) #TODO:// show prefix before Operation
admin.site.register(Operation, OperationAdmin)
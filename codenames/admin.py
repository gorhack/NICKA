from django.contrib import admin

# Register your models here.
from .models import Agency, Location, Operation

class AgencyAdmin(admin.ModelAdmin):
	fields=['name']

class LocationAdmin(admin.ModelAdmin):
	fields=['country', 'longitude', 'latitude']

class OperationAdmin(admin.ModelAdmin):
	fieldsets=[
		(None, {'fields':['code_word']}),
		('Operation Information', {'fields':['op_num','clearance','agency','user','location'],
									'classes':['collapse']}),
	]

admin.site.register(Agency, AgencyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Operation, OperationAdmin)
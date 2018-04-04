from django.contrib import admin
from .models import Companys,Ad

# class CompanyAdmin(admin.ModelAdmin):
# 	pass


admin.site.register(Companys)
admin.site.register(Ad)



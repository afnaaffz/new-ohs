from django.contrib import admin

from online_home_service_app import models

# Register your models here.
admin.site.register(models.Register)
admin.site.register(models.Login)
admin.site.register(models.Complaints)
admin.site.register(models.Register1)
admin.site.register(models.Schedule)
admin.site.register(models.Take_Appointment)
admin.site.register(models.Bill)
admin.site.register(models.CreditCard)
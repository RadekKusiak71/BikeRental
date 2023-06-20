from django.contrib import admin
from .models import UserProfile,Bike,RentOrder

admin.site.register(UserProfile)
admin.site.register(Bike)
admin.site.register(RentOrder)

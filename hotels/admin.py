from django.contrib import admin
from .models import *
# Register your models here.

class AdminHotel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
class AdminRoom(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('room_no',), }


admin.site.register(Hotel, AdminHotel)
admin.site.register(Room, AdminRoom)
admin.site.register(Review)
admin.site.register(ContactUs)
admin.site.register(PreBookRequest)

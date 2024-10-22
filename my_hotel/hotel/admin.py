from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class ImageBookingInline(admin.TabularInline):
    model = ImageBooking
    extra = 1


class BookingInline(admin.ModelAdmin):
    inlines = [ImageBookingInline]


admin.site.register(Booking, BookingInline)
admin.site.register(Hotel)
admin.site.register(ImageHotel)
admin.site.register(Room)
admin.site.register(ImageRoom)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(FavoriteHotel)


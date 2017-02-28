from django.contrib import admin

# Register your models here.

from .models import CalibVideo, Calib, User


class CalibInLine(admin.StackedInline):
    model = CalibVideo
    extra = 0

class CalibAdmin(admin.ModelAdmin):
    list_display = ('phonename', 'calib_text', 'calib_size')

    inlines = [CalibInLine]


class CalibVideoAdmin(admin.ModelAdmin):
    list_display = ('video_name', 'user', 'video_size', 'phonename')



admin.site.register(Calib, CalibAdmin)
admin.site.register(CalibVideo, CalibVideoAdmin)
admin.site.register(User)


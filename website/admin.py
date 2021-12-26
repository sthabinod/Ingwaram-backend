from django.contrib import admin
from .models import Company, Event,About, Front_Persons, History, Writer, Image
from django.utils.html import format_html


class EventImageAdmin(admin.StackedInline):
    model = Image

admin.site.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageAdmin]
    class Meta:
        model = Event

admin.site.register(About)
class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Front_Persons)
class FrontAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class EventImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="200" height="150" />'.format(obj.image.url))

    image_tag.short_description = 'image'
    list_display = ('image_tag','event')
    list_per_page = 3
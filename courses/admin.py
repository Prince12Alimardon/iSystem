from django.contrib import admin
from .models import Course, Contact, Isystem_in_numbers
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title', 'price')
    search_fields = ('id', 'title', 'price')
    list_filter = ('title',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'is_checked')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'phone', 'is_checked')
    list_filter = ('is_checked', 'name')


class Isystem_in_numbersAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_count', 'teachers_count', 'projects_count')
    list_display_links = ('id', 'course_count', 'teachers_count', 'projects_count')


admin.site.register(Course, CourseAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Isystem_in_numbers, Isystem_in_numbersAdmin)
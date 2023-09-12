from django.contrib import admin
from .models import Course, Category

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcom to the Courses admin area"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['creared_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'creared_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['creared_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)

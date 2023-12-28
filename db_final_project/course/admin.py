from django.contrib import admin
from .models import Course, Category, CourseCategories, Enrollment


admin.site.register(Course)
admin.site.register(Category)
admin.site.register(CourseCategories)
admin.site.register(Enrollment)

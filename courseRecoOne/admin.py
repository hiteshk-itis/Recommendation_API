from django.contrib import admin
from .models import Hero, CourseAnalytics, CourseInfo, CourseRating, Keywords, Tags, ServerCourse
# Register your models here.

admin.site.register(Hero)
admin.site.register(CourseAnalytics)
admin.site.register(CourseInfo)
admin.site.register(CourseRating)
admin.site.register(Keywords)
admin.site.register(Tags)
admin.site.register(ServerCourse)

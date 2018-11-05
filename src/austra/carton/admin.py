from django.contrib import admin

from carton.models import Course, Instructor, Session


class CourseAdmin(admin.ModelAdmin) :
	list_display = ("code", "name", "rating", "display_prereqs")

admin.site.register(Course, CourseAdmin)


class InstructorAdmin(admin.ModelAdmin) :
	list_display = ("name", "rating")

admin.site.register(Instructor, InstructorAdmin)

class SessionAdmin(admin.ModelAdmin) :
	list_display = ("course", "instructor", "max_seats", "get_rating")

admin.site.register(Session, SessionAdmin)

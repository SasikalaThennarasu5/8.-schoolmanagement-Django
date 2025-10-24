from django.contrib import admin
from .models import Teacher, Course, Student, Parent, Exam, Mark, Attendance

admin.site.site_header = 'School of Bright Futures - Admin'

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Exam)
admin.site.register(Mark)
admin.site.register(Attendance)

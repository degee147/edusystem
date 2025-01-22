from django.contrib import admin

from django.contrib import admin
from .models import Institution, Course, Student, Enrollment, Analytics

admin.site.register(Institution)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Analytics)


from django.contrib import admin
from .models import User, Student, LibraryHistory, FeesHistory

admin.site.register(User)
admin.site.register(Student)
admin.site.register(LibraryHistory)
admin.site.register(FeesHistory)

from django.contrib import admin

from .models import User,Education

class EducationInline(admin.StackedInline):
	model = Education
	extra = 3

class UserAdmin(admin.ModelAdmin):
	inlines = [EducationInline]	

admin.site.register(User, UserAdmin)

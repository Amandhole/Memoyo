#https://codepen.io/srees/pen/ZEzZQWm
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 

admin.site.site_header = "MEMOYO ADMIN"
admin.site.site_title = "MEMOYO ANIMATION"
admin.site.index_title = "Welcome to MEMOYO ADMIN"

class MyUserAdmin(BaseUserAdmin):
	fieldsets = (
		(None, {'fields': ('id', 'email', 'password', 'is_staff', 'last_login')}),
		('Permissions', {'fields': (
			'is_superuser',
			'groups', 
			'user_permissions',
		)}),
	)
	add_fieldsets = (
		(
			None,
			{
				'classes': ('wide',),
				'fields': ('email', 'password1', 'password2')
			}
		),
	)

	list_display = ('id', 'email', 'password', 'is_staff','last_login')
	readonly_fields = ('id',)
	list_filter = ('is_staff', 'is_superuser', 'groups')
	search_fields = ('email',)
	ordering = ('-id',)
	filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(MyUser, MyUserAdmin)


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'city', 'looking_for_work']
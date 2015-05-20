from django.contrib import admin
from bkmks.models import TaskItem


class TaskItemAdmin(admin.ModelAdmin):
	list_display = ('usern', 'taskn', 'due_date' , 'due_time',)
	class Meta:
		model = TaskItem
		
admin.site.register(TaskItem, TaskItemAdmin)
# admin.site.register(UserProfile)

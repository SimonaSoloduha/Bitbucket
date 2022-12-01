from django.contrib import admin

from app_staff.models import Part, Worker


class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_title')


admin.site.register(Part, PartAdmin)
admin.site.register(Worker, WorkerAdmin)

from django.contrib import admin
from django.template.response import TemplateResponse
from main import models

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronym', 'birthday', 'job', 'min_salary', 'photo')
    list_filter = ('job',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')
    list_filter = ('is_active',)

@admin.register(models.Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'time_enter', 'time_exit', 'notes')
    list_filter = ('employee',)

@admin.register(models.StatSummary)
class StatSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/stat_summary_change_list.html'
    date_hierarchy = 'date'
    
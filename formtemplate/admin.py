from django.contrib import admin
from . import models


@admin.register(models.DataDefine)
class DataDefineAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'name', 'source', ]


@admin.register(models.FormFields)
class FormFieldsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'template', 'col_title', 'col_name', ]


@admin.register(models.FormTemplate)
class FormTemplateAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'title', 'form_type', 'sort_num', 'create_time', ]


@admin.register(models.FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'template']


@admin.register(models.FormDataReportConf)
class FormDataReportConfAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'report_id', 'report_name']

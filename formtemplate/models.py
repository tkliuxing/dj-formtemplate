from django.utils import timezone
from django.db import models


class FormTemplate(models.Model):
    """模板"""
    baseconfig_category_prefix = "模板:"
    create_user = models.ForeignKey(
        'usercenter.User', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='+', verbose_name='创建人', help_text='创建人'
    )
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    title = models.CharField('模板标题', max_length=127, help_text='模板标题')
    sort_num = models.PositiveIntegerField('序号', default=1, help_text='序号')

    fields = models.ManyToManyField(
        'baseconfig.BaseConfigItem', blank=True,
        related_name="%(app_label)s_%(class)s_related", verbose_name='模板字段', help_text='模板字段'
    )

    display_fields = models.ManyToManyField(
        'baseconfig.BaseConfigItem', related_name="+", blank=True, verbose_name='显示字段', help_text='显示字段'
    )

    filter_fields = models.ManyToManyField(
        'baseconfig.BaseConfigItem', related_name="+", blank=True, verbose_name='查询字段', help_text='查询字段'
    )

    class Meta:
        abstract = True
        verbose_name = '模板'
        verbose_name_plural = verbose_name
        ordering = ['sort_num']

    def __str__(self):
        return self.title

    @property
    def create_user_display(self):
        return self.create_user.full_name if self.create_user else ''

    @property
    def create_time_display(self):
        return self.create_time.strftime('%Y-%m-%d %H:%M:%S')


class FormTemplateData(models.Model):
    """模板值"""
    create_user = models.ForeignKey(
        'usercenter.User', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='+', verbose_name='创建人', help_text='创建人'
    )
    create_time = models.DateTimeField('创建时间', default=timezone.now)

    values = models.ManyToManyField(
        'baseconfig.BaseConfigValue', verbose_name='模板字段的值', help_text='模板字段的值',
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
    )

    class Meta:
        abstract = True
        verbose_name = '模板值'
        verbose_name_plural = verbose_name

    @property
    def create_user_display(self):
        return self.create_user.full_name if self.create_user else ''

    @property
    def create_time_display(self):
        return self.create_time.strftime('%Y-%m-%d %H:%M:%S')


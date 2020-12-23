import uuid

from django.utils import timezone
from django.db import models


# 数据定义
class DataDefine(models.Model):
    """数据定义"""
    SOURCE = (
        (1, '数据字典'),
        (2, 'API'),
        (3, '配置'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    name = models.CharField('数据名称', max_length=64, null=False, help_text='数据名称')
    source = models.IntegerField('数据来源', choices=SOURCE, default=1)
    define = models.TextField('数据定义')


# 模版字段
class FormFields(models.Model):
    """模版字段"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    template = models.ForeignKey(
        'FormTemplate', related_name='fields', verbose_name='模版', on_delete=models.CASCADE)
    col_title = models.CharField('字段名称', max_length=20, null=False, help_text='字段名称')
    col_name = models.CharField('数据库字段名', max_length=16, null=False, help_text='数据库字段名')
    widget = models.CharField('控件类型', max_length=16, null=False, help_text='控件类型')
    widget_attr = models.CharField('控件属性', max_length=255, null=False, help_text='控件属性')
    verify_exp = models.CharField('校验表达式', max_length=255, null=False, help_text='校验表达式')
    data_source = models.ForeignKey('DataDefine', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    sort_num = models.PositiveIntegerField('序号', default=1, help_text='序号')
    width = models.IntegerField('宽度', default=0, help_text='宽度')


# 模板
class FormTemplate(models.Model):
    """模板"""
    FORM_TYPE = (
        (1, '单行表单'),
        (2, '多行表单'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    title = models.CharField('模板标题', max_length=127, help_text='模板标题')
    form_type = models.IntegerField('表单类型', choices=FORM_TYPE, default=1)
    sort_num = models.PositiveIntegerField('序号', default=1, help_text='序号')
    remark = models.CharField('备注', max_length=1023, null=True, blank=True, help_text='备注')

    class Meta:
        verbose_name = '模板'
        verbose_name_plural = verbose_name
        ordering = ['sort_num']

    def __str__(self):
        return self.title

    @property
    def create_time_display(self):
        return self.create_time.strftime('%Y-%m-%d %H:%M:%S')


# 表单数据表
class FormData(models.Model):
    """表单数据表"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    user = models.ForeignKey(
        'usercenter.User', related_name='user', verbose_name='用户', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey('usercenter.Department', related_name='department', verbose_name='部门',
                                   on_delete=models.SET_NULL, null=True, blank=True)
    template = models.ForeignKey(
        'FormTemplate', related_name='data', verbose_name='模版', on_delete=models.SET_NULL, null=True, blank=True)
    field_01 = models.CharField('Field 01', max_length=1023, null=True, blank=True, db_index=True)
    field_02 = models.CharField('Field 02', max_length=1023, null=True, blank=True, db_index=True)
    field_03 = models.CharField('Field 03', max_length=1023, null=True, blank=True, db_index=True)
    field_04 = models.CharField('Field 04', max_length=1023, null=True, blank=True, db_index=True)
    field_05 = models.CharField('Field 05', max_length=1023, null=True, blank=True, db_index=True)
    field_06 = models.CharField('Field 06', max_length=1023, null=True, blank=True)
    field_07 = models.CharField('Field 07', max_length=1023, null=True, blank=True)
    field_08 = models.CharField('Field 08', max_length=1023, null=True, blank=True)
    field_09 = models.CharField('Field 09', max_length=1023, null=True, blank=True)
    field_10 = models.CharField('Field 10', max_length=1023, null=True, blank=True)
    field_11 = models.CharField('Field 11', max_length=1023, null=True, blank=True)
    field_12 = models.CharField('Field 12', max_length=1023, null=True, blank=True)
    field_13 = models.CharField('Field 13', max_length=1023, null=True, blank=True)
    field_14 = models.CharField('Field 14', max_length=1023, null=True, blank=True)
    field_15 = models.CharField('Field 15', max_length=1023, null=True, blank=True)
    field_16 = models.CharField('Field 16', max_length=1023, null=True, blank=True)
    field_17 = models.CharField('Field 17', max_length=1023, null=True, blank=True)
    field_18 = models.CharField('Field 18', max_length=1023, null=True, blank=True)
    field_19 = models.CharField('Field 19', max_length=1023, null=True, blank=True)
    field_20 = models.CharField('Field 20', max_length=1023, null=True, blank=True)
    field_21 = models.CharField('Field 21', max_length=1023, null=True, blank=True)
    field_22 = models.CharField('Field 22', max_length=1023, null=True, blank=True)
    field_23 = models.CharField('Field 23', max_length=1023, null=True, blank=True)
    field_24 = models.CharField('Field 24', max_length=1023, null=True, blank=True)
    field_25 = models.CharField('Field 25', max_length=1023, null=True, blank=True)
    field_26 = models.CharField('Field 26', max_length=1023, null=True, blank=True)
    field_27 = models.CharField('Field 27', max_length=1023, null=True, blank=True)
    field_28 = models.CharField('Field 28', max_length=1023, null=True, blank=True)
    field_29 = models.CharField('Field 29', max_length=1023, null=True, blank=True)
    field_30 = models.CharField('Field 30', max_length=1023, null=True, blank=True)

    date_01 = models.DateField('Date 01', null=True, blank=True, db_index=True)
    date_02 = models.DateField('Date 02', null=True, blank=True, db_index=True)
    date_03 = models.DateField('Date 03', null=True, blank=True, db_index=True)
    date_04 = models.DateField('Date 04', null=True, blank=True, db_index=True)
    date_05 = models.DateField('Date 05', null=True, blank=True, db_index=True)
    date_06 = models.DateField('Date 06', null=True, blank=True)
    date_07 = models.DateField('Date 07', null=True, blank=True)
    date_08 = models.DateField('Date 08', null=True, blank=True)
    date_09 = models.DateField('Date 09', null=True, blank=True)
    date_10 = models.DateField('Date 10', null=True, blank=True)

    datetime_01 = models.DateTimeField('DateTime 01', null=True, blank=True, db_index=True)
    datetime_02 = models.DateTimeField('DateTime 02', null=True, blank=True, db_index=True)
    datetime_03 = models.DateTimeField('DateTime 03', null=True, blank=True, db_index=True)
    datetime_04 = models.DateTimeField('DateTime 04', null=True, blank=True, db_index=True)
    datetime_05 = models.DateTimeField('DateTime 05', null=True, blank=True, db_index=True)
    datetime_06 = models.DateTimeField('DateTime 06', null=True, blank=True)
    datetime_07 = models.DateTimeField('DateTime 07', null=True, blank=True)
    datetime_08 = models.DateTimeField('DateTime 08', null=True, blank=True)
    datetime_09 = models.DateTimeField('DateTime 09', null=True, blank=True)
    datetime_10 = models.DateTimeField('DateTime 10', null=True, blank=True)

    int_01 = models.BigIntegerField('Int 01', null=True, blank=True, db_index=True)
    int_02 = models.BigIntegerField('Int 02', null=True, blank=True, db_index=True)
    int_03 = models.BigIntegerField('Int 03', null=True, blank=True, db_index=True)
    int_04 = models.BigIntegerField('Int 04', null=True, blank=True, db_index=True)
    int_05 = models.BigIntegerField('Int 05', null=True, blank=True, db_index=True)
    int_06 = models.BigIntegerField('Int 06', null=True, blank=True)
    int_07 = models.BigIntegerField('Int 07', null=True, blank=True)
    int_08 = models.BigIntegerField('Int 08', null=True, blank=True)
    int_09 = models.BigIntegerField('Int 09', null=True, blank=True)
    int_10 = models.BigIntegerField('Int 10', null=True, blank=True)

    float_01 = models.DecimalField('Float 01', max_digits=16, decimal_places=4, null=True, blank=True, db_index=True)
    float_02 = models.DecimalField('Float 02', max_digits=16, decimal_places=4, null=True, blank=True, db_index=True)
    float_03 = models.DecimalField('Float 03', max_digits=16, decimal_places=4, null=True, blank=True)
    float_04 = models.DecimalField('Float 04', max_digits=16, decimal_places=4, null=True, blank=True)
    float_05 = models.DecimalField('Float 05', max_digits=16, decimal_places=4, null=True, blank=True)
    float_06 = models.DecimalField('Float 06', max_digits=16, decimal_places=4, null=True, blank=True)
    float_07 = models.DecimalField('Float 07', max_digits=16, decimal_places=4, null=True, blank=True)
    float_08 = models.DecimalField('Float 08', max_digits=16, decimal_places=4, null=True, blank=True)
    float_09 = models.DecimalField('Float 09', max_digits=16, decimal_places=4, null=True, blank=True)
    float_10 = models.DecimalField('Float 10', max_digits=16, decimal_places=4, null=True, blank=True)

    text_01 = models.TextField('Text_01', null=True, blank=True)
    text_02 = models.TextField('Text_02', null=True, blank=True)
    text_03 = models.TextField('Text_03', null=True, blank=True)
    text_04 = models.TextField('Text_04', null=True, blank=True)
    text_05 = models.TextField('Text_05', null=True, blank=True)

    class Meta:
        verbose_name = 'Form数据表'
        verbose_name_plural = verbose_name


# 表单数据报表
class FormDataReportConf(models.Model):
    """表单数据报表"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    report_id = models.IntegerField('报表ID', default=1, db_index=True, unique=True)
    report_name = models.CharField('报表名称', max_length=31, null=True, blank=True, db_index=True, help_text='报表名称')
    report_remark = models.TextField('报表说明', null=True, blank=True, help_text='报表说明')
    form_template = models.ForeignKey('FormTemplate', on_delete=models.SET_NULL, null=True, blank=True)
    arguments = models.TextField('参数定义', null=True, blank=True, help_text='参数定义')
    data_struct = models.TextField('数据定义', null=True, blank=True, help_text='数据定义')
    charts_struct = models.TextField('图表定义', null=True, blank=True, help_text='图表定义')

    class Meta:
        verbose_name = '数据报表'
        verbose_name_plural = verbose_name

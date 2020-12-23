from rest_framework.serializers import ModelSerializer
from . import models


class DataDefineSerializer(ModelSerializer):

    class Meta:
        model = models.DataDefine
        fields = (
            'pk',
            'sys_id',
            'org_id',
            'biz_id',
            'name',
            'source',
            'define',
        )


class FormFieldsSerializer(ModelSerializer):

    class Meta:
        model = models.FormFields
        fields = (
            'pk',
            'sys_id',
            'org_id',
            'biz_id',
            'template',
            'col_title',
            'col_name',
            'widget',
            'widget_attr',
            'verify_exp',
            'data_source',
            'sort_num',
            'width',
        )


class FormTemplateSerializer(ModelSerializer):

    class Meta:
        model = models.FormTemplate
        fields = (
            'pk',
            'sys_id',
            'org_id',
            'biz_id',
            'create_time',
            'title',
            'form_type',
            'sort_num',
            'remark',
        )


class FormDataSerializer(ModelSerializer):

    class Meta:
        model = models.FormData
        fields = (
            'pk',
            'sys_id',
            'org_id',
            'biz_id',
            'user',
            'department',
            'template',
            'field_01',
            'field_02',
            'field_03',
            'field_04',
            'field_05',
            'field_06',
            'field_07',
            'field_08',
            'field_09',
            'field_10',
            'field_11',
            'field_12',
            'field_13',
            'field_14',
            'field_15',
            'field_16',
            'field_17',
            'field_18',
            'field_19',
            'field_20',
            'field_21',
            'field_22',
            'field_23',
            'field_24',
            'field_25',
            'field_26',
            'field_27',
            'field_28',
            'field_29',
            'field_30',
            'date_01',
            'date_02',
            'date_03',
            'date_04',
            'date_05',
            'date_06',
            'date_07',
            'date_08',
            'date_09',
            'date_10',
            'datetime_01',
            'datetime_02',
            'datetime_03',
            'datetime_04',
            'datetime_05',
            'datetime_06',
            'datetime_07',
            'datetime_08',
            'datetime_09',
            'datetime_10',
            'int_01',
            'int_02',
            'int_03',
            'int_04',
            'int_05',
            'int_06',
            'int_07',
            'int_08',
            'int_09',
            'int_10',
            'float_01',
            'float_02',
            'float_03',
            'float_04',
            'float_05',
            'float_06',
            'float_07',
            'float_08',
            'float_09',
            'float_10',
            'text_01',
            'text_02',
            'text_03',
            'text_04',
            'text_05',
        )


class FormDataReportConfSerializer(ModelSerializer):

    class Meta:
        model = models.FormDataReportConf
        fields = (
            'pk',
            'sys_id',
            'org_id',
            'biz_id',
            'report_id',
            'report_name',
            'report_remark',
            'form_template',
            'arguments',
            'data_struct',
            'charts_struct',
        )

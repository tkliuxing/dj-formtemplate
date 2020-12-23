from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models
from . import filters


class FormDataDefineViewSet(ModelViewSet):
    """数据定义"""
    queryset = models.DataDefine.objects.order_by('pk')
    serializer_class = serializers.DataDefineSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sys_id', 'org_id', 'biz_id', 'name', 'source',)


class FormFieldsViewSet(ModelViewSet):
    """模版字段"""
    queryset = models.FormFields.objects.order_by('pk')
    serializer_class = serializers.FormFieldsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sys_id', 'org_id', 'biz_id', 'template',)


class FormTemplateViewSet(ModelViewSet):
    """模板"""
    queryset = models.FormTemplate.objects.order_by('pk')
    serializer_class = serializers.FormTemplateSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sys_id', 'org_id', 'biz_id', 'title', 'form_type',)


class FormDataViewSet(ModelViewSet):
    """表单数据表"""
    queryset = models.FormData.objects.order_by('pk')
    serializer_class = serializers.FormDataSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.FormDataFilterSet


class FormDataReportConfViewSet(ModelViewSet):
    """表单数据报表"""
    queryset = models.FormDataReportConf.objects.order_by('pk')
    serializer_class = serializers.FormDataReportConfSerializer

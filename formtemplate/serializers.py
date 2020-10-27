from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from baseconfig.serializers import BaseConfigItemSerializer, BaseConfigValueSerializer
from . import models


class TemplateBaseSerializer(ModelSerializer):
    fields_info = BaseConfigItemSerializer(
        many=True, source='fields', read_only=True
    )
    display_fields_info = BaseConfigItemSerializer(
        many=True, source='display_fields', read_only=True
    )
    filter_fields_info = BaseConfigItemSerializer(
        many=True, source='filter_fields', read_only=True
    )

    class Meta:
        model = models.FormTemplate
        fields = (
            'pk',
            'baseconfig_category_prefix',
            'fields',
            'fields_info',
            'display_fields',
            'display_fields_info',
            'filter_fields',
            'filter_fields_info',
            'create_time',
            'create_time_display',
            'create_user',
            'create_user_display',
            'title',
            'sort_num',
        )


class TemplateDataBaseSerializer(ModelSerializer):
    input_values = serializers.JSONField(write_only=True)
    values = BaseConfigValueSerializer(many=True, read_only=True)
    values_dict = serializers.SerializerMethodField(help_text='表单值，按BaseConfigItem的pk为key，BaseConfigValue为value')
    values_name_dict = serializers.SerializerMethodField(help_text='表单值，按BaseConfigItem的name为key，BaseConfigValue为value')

    class Meta:
        model = models.FormTemplateData
        fields = (
            'pk',
            'create_user',
            'create_user_display',
            'create_time',
            'create_time_display',
            'input_values',
            'values',
            'values_dict',
            'values_name_dict',
        )

    def create(self, validated_data):
        input_values = validated_data.pop('input_values')
        instance = self.Meta.model.objects.create(**validated_data)
        for k, v in input_values.items():
            value_serializer = BaseConfigValueSerializer(data={'item': k, 'value': v})
            if value_serializer.is_valid():
                instance.values.add(value_serializer.save())
        return instance

    def update(self, instance, validated_data):
        if 'input_values' in validated_data:
            input_values = validated_data.pop('input_values')
        else:
            input_values = {}
        instance = super().update(instance, validated_data)
        for k, v in input_values.items():
            values = instance.values.filter(item_id=k)
            if values:
                value = values[0]
                value_serializer = BaseConfigValueSerializer(data={'item': k, 'value': v}, instance=value)
                if value_serializer.is_valid():
                    value_serializer.save()
            else:
                value_serializer = BaseConfigValueSerializer(data={'item': k, 'value': v})
                if value_serializer.is_valid():
                    instance.values.add(value_serializer.save())
        return instance

    def get_values_dict(self, obj):
        return {
            i.item.pk: BaseConfigValueSerializer(i).data
            for i in obj.values.all()
        }

    def get_values_name_dict(self, obj):
        return {
            i.item.name: i.value_display
            for i in obj.values.all()
        }

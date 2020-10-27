import django_filters
from . import models


class TemplateBaseDataFilterSet(django_filters.FilterSet):
    class Meta:
        fields = (
            'create_user',
            'create_time',
        )

    def filter_queryset(self, queryset):
        from baseconfig.models import BaseConfigItem
        qs = super().filter_queryset(queryset)
        request = self.request
        for k, v in request.GET.items():
            if not k.isnumeric() and ('_' not in k):
                continue
            if v == '':
                continue
            if k.isnumeric():
                try:
                    baseconfig_item = BaseConfigItem.objects.get(pk=k)
                except BaseConfigItem.DoesNotExist:
                    continue
                if baseconfig_item.item_type == 'str' and not baseconfig_item.is_choices:
                    qs = qs.filter(values__item=k, values__str_value__contains=v)
                elif baseconfig_item.is_choices and not baseconfig_item.is_multiple_choices:
                    qs = qs.filter(values__item=k, values__choices_value=v)
                elif baseconfig_item.is_choices and baseconfig_item.is_multiple_choices:
                    qs = qs.filter(values__item=k, values__multi_choices_value=v)
                else:
                    # TODO: 多种类型的筛选
                    qs = qs.filter(values__item=k, values__raw_value=v)
                continue
            k_args = k.split('_')
            if len(k_args) == 1 or not k_args[0].isnumeric():
                continue
            if len(k_args) == 2:
                item_id = k_args[0]
                try:
                    baseconfig_item = BaseConfigItem.objects.get(pk=item_id)
                except BaseConfigItem.DoesNotExist:
                    continue
                if k_args[1] == 'from':
                    if baseconfig_item.item_type == 'date':
                        qs = qs.filter(values__item=item_id, values__date_value__gte=v)
                    if baseconfig_item.item_type == 'datetime':
                        qs = qs.filter(values__item=item_id, values__datetime_value__gte=v)
                if k_args[1] == 'to':
                    if baseconfig_item.item_type == 'date':
                        qs = qs.filter(values__item=item_id, values__date_value__lte=v)
                    if baseconfig_item.item_type == 'datetime':
                        qs = qs.filter(values__item=item_id, values__datetime_value__lte=v)
                continue
        return qs

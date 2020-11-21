from .search_indexes import ConfigMenuIndex, DataapiConfigMenuBpIndex, DtechartsConfigMenuIndex
from drf_haystack.serializers import HaystackSerializer


class ConfigMenuIndexSerializer(HaystackSerializer):
    """
    SKU索引结果数据序列化器
    """
    class Meta:
        index_classes = [ConfigMenuIndex, DataapiConfigMenuBpIndex, DtechartsConfigMenuIndex]
        fields = ('text', 'name', 'url', 'url_type', 'status', 'chart_type')

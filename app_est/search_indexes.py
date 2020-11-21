from .models import ConfigMenu, DataapiConfigmenuBp, DtechartsConfigMenu
from haystack import indexes


# 修改此处，类名为模型类的名称+Index
class ConfigMenuIndex(indexes.SearchIndex, indexes.Indexable):
    # text为索引字段
    # document = True，这代表haystack和搜索引擎将使用此字段的内容作为索引进行检索
    # use_template=True 指定根据表中的那些字段建立索引文件的说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)
    # 模型字段,打包数据
    name = indexes.CharField(model_attr='name')
    url = indexes.CharField(model_attr='url')
    url_type = indexes.IntegerField(model_attr='url_type')
    status = indexes.IntegerField(model_attr='status')
    chart_type = indexes.CharField(model_attr='chart_type')

    # 对那张表进行查询
    def get_model(self):
        # 重载get_model方法，必须要有！
        return ConfigMenu  # 返回这个model

    def index_queryset(self, using=None):
        # 这里是对url_type不等于0的字段建立索引
        # return self.get_model().objects.exclude(url_type=0)
        return self.get_model().objects.all()


class DataapiConfigMenuBpIndex(indexes.SearchIndex, indexes.Indexable):
    # text为索引字段
    # document = True，这代表haystack和搜索引擎将使用此字段的内容作为索引进行检索
    # use_template=True 指定根据表中的那些字段建立索引文件的说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)
    # 模型字段,打包数据
    name = indexes.CharField(model_attr='name')
    url = indexes.CharField(model_attr='url')
    url_type = indexes.IntegerField(model_attr='url_type')
    status = indexes.IntegerField(model_attr='status')
    chart_type = indexes.CharField(model_attr='chart_type')

    # 对那张表进行查询
    def get_model(self):
        # 重载get_model方法，必须要有！
        return DataapiConfigmenuBp  # 返回这个model

    def index_queryset(self, using=None):
        # 这个方法返回什么内容，最终就会对那些方法建立索引，这里是对所有字段建立索引
        return self.get_model().objects.all()


class DtechartsConfigMenuIndex(indexes.SearchIndex, indexes.Indexable):
    # text为索引字段
    # document = True，这代表haystack和搜索引擎将使用此字段的内容作为索引进行检索
    # use_template=True 指定根据表中的那些字段建立索引文件的说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)
    # 模型字段,打包数据
    name = indexes.CharField(model_attr='name')
    url = indexes.CharField(model_attr='url')
    url_type = indexes.IntegerField(model_attr='url_type')
    status = indexes.IntegerField(model_attr='status')
    chart_type = indexes.CharField(model_attr='chart_type')

    # 对那张表进行查询
    def get_model(self):
        # 重载get_model方法，必须要有！
        return DtechartsConfigMenu  # 返回这个model

    def index_queryset(self, using=None):
        # 这个方法返回什么内容，最终就会对那些方法建立索引，这里是对所有字段建立索引
        return self.get_model().objects.all()

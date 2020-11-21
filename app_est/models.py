from django.db import models

# Create your models here.
class ConfigMenu(models.Model):
    name = models.CharField(
        verbose_name='节点名称',
        max_length=255)
    parentId = models.IntegerField(verbose_name='父Id')
    synonym_describe = models.CharField(
        verbose_name='近义词',
        max_length=255,
        null=True)
    level = models.IntegerField('层级')
    url = models.CharField(max_length=255, null=True)
    url_type = models.IntegerField(
        choices=((0, '无类型'), (1, '数据接口'), (2, '产业链截图'), (3, 'dtApp截图'), (4, 'gif动图')),
        default=0)
    status = models.IntegerField(
        choices=((0, '失效'), (1, '可用')),
        default=1,
        verbose_name='可用状态')
    chart_type = models.CharField(
        verbose_name='图表类型',
        max_length=25,
        default='',
        blank=True)

    def parent_node_name(self):
        return ConfigMenu.objects.get(id=self.parentId)

    parent_node_name.short_description = '父节点名称'

    class Meta:
        verbose_name = '魔方菜单'
        verbose_name_plural = verbose_name
        db_table = 'dataapi_configmenu'

    def __str__(self):
        return self.name


class DataapiConfigmenuBp(models.Model):
    name = models.CharField(max_length=255)
    synonym_describe = models.CharField(max_length=255, blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
    level = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    url_type = models.IntegerField(blank=True, null=True)
    chart_type = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'dataapi_configmenu_bp'


class DtechartsConfigMenu(models.Model):
    name = models.CharField(max_length=255)
    synonym_describe = models.CharField(max_length=255, blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
    level = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    url_type = models.IntegerField(blank=True, null=True)
    chart_type = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'dtecharts_config_menu'

from django.shortcuts import render, HttpResponse
from drf_haystack.viewsets import HaystackViewSet
from .models import ConfigMenu, DataapiConfigmenuBp, DtechartsConfigMenu
from .serializers import ConfigMenuIndexSerializer
import os
# Create your views here.


class ConfigMenuSearchViewSet(HaystackViewSet):    # HaystackViewSet继承了RetrieveModelMixin, ListModelMixin, ViewSetMixin, HaystackGenericAPIView，所以可以查一条或多条数据
    """
    ConfigMenu搜索
    HaystackViewSet： 查一条，查多条
    """
    index_models = [ConfigMenu, DataapiConfigmenuBp, DtechartsConfigMenu]
    serializer_class = ConfigMenuIndexSerializer


def IndexRebuild(request):
    if request.method == "GET":
        path = os.getcwd()
        print(path)
        # val = os.system("echo y |python manage.py rebuild_index")
        val = os.popen('echo y |python manage.py rebuild_index').read()
        return HttpResponse(val)

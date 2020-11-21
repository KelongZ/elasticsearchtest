from django.shortcuts import render, HttpResponse
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"err_msg": "success", "code": "200", "data": serializer.data})


def IndexRebuild(request):
    if request.method == "GET":
        path = os.getcwd()
        print(path)
        # val = os.system("echo y |python manage.py rebuild_index")
        val = os.popen('echo y |python manage.py rebuild_index').read()
        return HttpResponse(val)

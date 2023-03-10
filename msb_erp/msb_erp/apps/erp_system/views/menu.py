import logging

from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from erp_system.models import MenuModel
from rest_framework.response import Response
from msb_erp.apps.erp_system.serializer.menu_serializer import MenuSerializer

logger = logging.getLogger('erp')

"""
功能菜单的视图类

1 新增
2 查询单个功能菜单
3 查询所有功能菜单
4 查询某个父菜单下面的所有子菜单列表
5 查询所有顶级菜单列表
6 删除某一个功能菜单
7 批量删除多个功能菜单  传参:[x,y,z]
8 修改功能菜单
"""


class MenuView(viewsets.ModelViewSet):
    """
    create:
    新增菜单,

    参数: menu对象,其中delete_flag,cerate_time,update_time 不用传参,return:添加之后的对象

    retrieve:
    查询单个菜单对象

    list:
    查询所有的菜单

    如果参数中有Pid,则查询某一个父菜单列表,pid=0表示查询项目顶级菜单列表

    update:
    修改菜单

    destroy:
    删除指定id的菜单

    multiple_delete:
    批量删除菜单

    参数: 传参要求是个id列表[id1,id2,id3,...]

    partial_update:
    局部修改菜单,修改任意指定的属性
    """

    queryset = MenuModel.objects.filter(delete_flag=0).all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        """
        两种情况:
        1 查询所有菜单列表,不要传任何参数
        2 查询某个父菜单下面的所有子菜单列表,需要传递一个参数,名字叫pid,pid==0时:查询所有顶级菜单列表
        :return:
        """
        query_param = self.request.query_params.get('pid', None)
        if query_param:
            pid = int(query_param)
            if pid == 0:  # 查询所有顶级菜单列表
                return MenuModel.objects.filter(parent__isnull=True, delete_flag='0').all()
            else:  # 查询某个父菜单下面的所有子菜单列表
                return MenuModel.objects.filter(parent_id=pid).all()
        else:
            return MenuModel.objects.filter(delete_flag=0).all()

    def destroy(self, request, *args, **kwargs):
        # 修改一下删除标记,delete_flag = 1
        menu = self.get_object()
        menu.delete_flag = '1'
        menu.save()
        # 可能该菜单下面,还有很多子菜单,这些子菜单也要修改
        MenuModel.objects.filter(parent_id=menu.id).update(delete_flag=1)
        return Response(status=status.HTTP_204_NO_CONTENT)

    del_ids = openapi.Schema(type=openapi.TYPE_OBJECT, required=['ids'], properties={
        'ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_INTEGER),
                              description='选择哪些需要删除的id列表')
    })

    # action装饰器可以接收两个参数：
    # methods: 声明该action对应的请求方式，列表传递
    # detail: 声明该action的路径是否与单一资源对应，及是否是xxx/<pk>/action方法名/
    #     True 表示路径格式是xxx/<pk>/action方法名/
    #     False 表示路径格式是xxx/action方法名/
    @swagger_auto_schema(method='delete', request_body=del_ids,
                         operation_description='批量删除菜单 参数: 传参要求是个id列表[id1,id2,id3,...]')
    @action(methods=['delete'], detail=False)
    def multiple_delete(self, request, *args, **kwargs):
        delete_ids = request.data.get('ids')
        if not delete_ids:
            return Response(data={'detail': '参数错误,ids为必传参数'}, status=status.HTTP_400_BAD_REQUEST)
        elif not isinstance(delete_ids, list):
            return Response(data={'detail': 'ids格式错误,必须为List'}, status=status.HTTP_400_BAD_REQUEST)

        # 首先删除传递过来的菜单
        MenuModel.objects.filter(id__in=delete_ids).update(delete_flag=1)
        MenuModel.objects.filter(parent_id__in=delete_ids).update(delete_flag=1)
        return Response(status=status.HTTP_204_NO_CONTENT)

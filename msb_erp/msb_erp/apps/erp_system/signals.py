import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from erp_system.models import MenuModel, PermissionsModel

logger = logging.getLogger('erp')
methods = {'POST': '新增', 'GET': '查询', 'PUT': '修改', 'DELETE': '删除', 'PATCH': '改局部'}


@receiver(post_save, sender=MenuModel)
def create_menu_permission(sender, instance, created, **kwargs):
    # 此处有BUG:父级菜单和子级菜单修改的时候会出现不会对权限进行新增或删除
    """
    创建信号监控函数,信号接收者收到之后自动触发.创建菜单资源对应的权限
    """
    if created:
        if isinstance(instance, MenuModel):
            if not instance.parent:  # 因为不是父菜单,那么menu就是功能块菜单对象
                permission = PermissionsModel.objects.create(name=instance.name + '的权限', is_menu=True)
                permission.menu = instance
                permission.save()
                return logger.info('创建了功能块菜单对象,已在MenuModel中插入了数据,但是没有提供权限')
            else:  # 当前菜单是接口
                for method in methods.keys():
                    permission = PermissionsModel.objects.create(name=methods.get(method),
                                                                 desc=f'{instance.name}的{methods.get(method)}的权限',
                                                                 is_menu=False, method=method, path=instance.url)
                    permission.menu = instance
                    permission.save()
                return logger.info('已创建菜单资源对应的权限')

        else:
            return logger.warning('当前对象不是MenuModel类型,所以不需要创建对应的权限!')
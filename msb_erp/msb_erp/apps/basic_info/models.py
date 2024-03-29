from django.db import models

from msb_erp.utils.base_model import BaseModel, BaseModel2


# Create your models here.

class Nation(models.Model):
    id = models.IntegerField(primary_key=True)
    n_name = models.CharField('国家名称', max_length=30)

    class Meta:
        db_table = 'nation'
        verbose_name = '国家表'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.n_name


class Province(models.Model):
    id = models.IntegerField(primary_key=True)
    p_name = models.CharField('省份名称', max_length=30)
    nation = models.ForeignKey(to=Nation, related_name='province_list', on_delete=models.CASCADE)

    class Meta:
        db_table = 'province'
        verbose_name = '省份表'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.p_name


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    c_name = models.CharField('省份名称', max_length=30)
    province = models.ForeignKey(to=Province, related_name='city_list', on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'
        verbose_name = '城市表'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.c_name


# 供应商模型类
class SupplierModel(BaseModel2):
    name = models.CharField(max_length=100, verbose_name='供应商名称', unique=True)
    mobile = models.CharField('手机号码', max_length=11)
    phone = models.CharField('联系电话', max_length=22)
    contacts_name = models.CharField('联系人名', max_length=22)
    email = models.CharField('电子邮箱', max_length=50)
    ratepayer_number = models.CharField('纳税人识别号码', max_length=50)
    bank = models.CharField('开户银行', max_length=50)
    account_number = models.CharField('银行账号', max_length=50)
    nation = models.CharField('国家', max_length=50)
    province = models.CharField('省份', max_length=50)
    city = models.CharField('城市', max_length=50)
    address = models.CharField('详细地址', max_length=50)
    remark = models.CharField('备注', max_length=512)
    init_pay = models.DecimalField('初期应付', max_digits=20, decimal_places=2)  # 精确到小数点后两位
    current_pay = models.DecimalField('末期应付', max_digits=20, decimal_places=2)  # 精确到小数点后两位
    order_number = models.IntegerField('排序号码', default=100)

    class Meta:
        db_table = 't_supplier'
        verbose_name = '供应商'
        verbose_name_plural = verbose_name
        ordering = ['order_number', 'id']

    def __str__(self):
        return self.name


# 客户模型类
class CustomerModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name='客户名称', unique=True)
    mobile = models.CharField('手机号码', max_length=11, blank=True, null=True)
    phone = models.CharField('联系电话', max_length=22, blank=True, null=True)
    contacts_name = models.CharField('联系人名', max_length=22, blank=True, null=True)
    email = models.CharField('电子邮箱', max_length=50, blank=True, null=True)
    ratepayer_number = models.CharField('纳税人识别号码', max_length=50, blank=True, null=True)
    bank = models.CharField('开户银行', max_length=50, blank=True, null=True)
    account_number = models.CharField('银行账号', max_length=50, blank=True, null=True)
    nation = models.CharField('国家', max_length=50, blank=True, null=True)
    province = models.CharField('省份', max_length=50, blank=True, null=True)
    city = models.CharField('城市', max_length=50, blank=True, null=True)
    address = models.CharField('详细地址', max_length=50, blank=True, null=True)
    remark = models.CharField('备注', max_length=512, blank=True, null=True)
    init_receivable = models.DecimalField('初期应收', max_digits=20, decimal_places=2, blank=True,
                                          null=True)  # 精确到小数点后两位
    current_receivable = models.DecimalField('末期应收', max_digits=20, decimal_places=2, blank=True,
                                             null=True)  # 精确到小数点后两位
    order_number = models.IntegerField('排序号码', default=100)

    class Meta:
        db_table = 't_customer'
        verbose_name = '客户'
        verbose_name_plural = verbose_name
        ordering = ['order_number', 'id']

    def __str__(self):
        return self.name


# 仓库模型类
class WarehouseModel(BaseModel2):
    name = models.CharField(max_length=100, verbose_name='仓库名称', unique=True)
    nation = models.CharField('国家', max_length=50, blank=True, null=True)
    province = models.CharField('省份', max_length=50, blank=True, null=True)
    city = models.CharField('城市', max_length=50, blank=True, null=True)
    address = models.CharField('详细地址', max_length=50, blank=True, null=True)
    remark = models.CharField('备注', max_length=512, blank=True, null=True)
    warehouse_fee = models.DecimalField('仓储费用(元/天/KG)', max_digits=10, decimal_places=2, blank=True,
                                        null=True)  # 精确到小数点后两位
    truckage = models.DecimalField('搬运费用', max_digits=10, decimal_places=2, blank=True, null=True)  # 精确到小数点后两位
    order_number = models.IntegerField('排序号码', default=100)
    is_default = models.BooleanField('是否默认的仓库', default=False)
    # 用户模型来自于erp_system的APP中，必须要加前缀
    leader_user = models.ForeignKey('erp_system.UserModel', null=True, blank=True, on_delete=models.SET_NULL,
                                    verbose_name='仓库负责人')

    class Meta:
        db_table = 't_warehouse'
        verbose_name = '仓库'
        verbose_name_plural = verbose_name
        ordering = ['order_number', 'id']

    def __str__(self):
        return self.name


# 结算账户模型类
class SettlementAccountModel(BaseModel2):
    name = models.CharField(max_length=100, verbose_name='仓库名称', unique=True)
    number_code = models.CharField('编号', max_length=28, unique=True)
    remark = models.CharField('备注', max_length=512, blank=True, null=True)
    init_amount = models.DecimalField('初期金额', max_digits=10, decimal_places=2, blank=True, null=True)  # 精确到小数点后两位
    balance = models.DecimalField('余额', max_digits=10, decimal_places=2, blank=True, null=True)  # 精确到小数点后两位
    order_number = models.IntegerField('排序号码', default=100)
    is_default = models.BooleanField('是否默认', default=False)

    class Meta:
        db_table = 't_settlement_account'
        verbose_name = '仓库'
        verbose_name_plural = verbose_name
        ordering = ['order_number', 'id']

    def __str__(self):
        return self.name
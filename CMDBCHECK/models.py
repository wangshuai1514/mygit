from django.db import models

# Create your models here.
class Server(models.Model):
    server_type_choice = (
        (0,'PC服务器'),
        (1,'刀片机'),
        (2,'小型机')
    )
    created_by_choice = (
        ('auto','自动添加'),
        ('manual','手工录入')
    )
    server_type = models.SmallIntegerField(choices=server_type_choice,
                                           default=0,
                                           verbose_name='服务器类型')
    created_by = models.CharField(choices=created_by_choice,
                                max_length=32,
                                default='auto',
                                verbose_name='添加方式')
    IP = models.CharField(verbose_name='IP地址',max_length=30,default='')
    MAC = models.CharField(verbose_name='Mac地址',max_length=200,null=True,blank=True,default='')
    hostname = models.CharField(max_length=128, null=True, blank=True, verbose_name="主机名")
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器型号')

    os_type = models.CharField(verbose_name='操作系统类型', max_length=64, blank=True, null=True)
# os_distribution: Redhat 8 , Centos 7, Windows10, Windows8
    os_distribution = models.CharField(verbose_name='发行商', max_length=64, blank=True, null=True)
    os_release = models.CharField(verbose_name='操作系统版本', max_length=64, blank=True, null=True)
    sn = models.CharField(verbose_name='资产标识', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.IP
    class Meta:
        db_table = 'servers'
        verbose_name = "服务器管理"
        verbose_name_plural = "服务器管理"
class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=30, default='root')
    password = models.CharField(verbose_name="密码", max_length=40, default='123')
    pkey = models.CharField(verbose_name="私钥", max_length=40, default='id_rsa')
    server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name="所属服务器")

    def __str__(self):
        return self.username
    class Meta:
        # 设置数据库表的名称，默认情况下表名是APP名称_models类名
        db_table = 'users'
        verbose_name = "服务器用户管理"
        verbose_name_plural = "服务器用户管理"
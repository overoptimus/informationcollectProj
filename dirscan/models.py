from django.db import models


# Create your models here.

class Dir_domain_manager(models.Manager):
    def isExists(self, domainName=''):
        try:
            super(Dir_domain_manager, self).get(domain=domainName)
        except:
            return False
        return True
    # 已经有了create方法，不需要再写一次了
    # def create(self, domain, file_ext):
    #     dir_domain = self.model()
    #     dir_domain.domain = domain
    #     dir_domain.file_ext = file_ext
    #     return dir_domain

class Dir_domain(models.Model):
    objects = Dir_domain_manager()
    domain = models.CharField(max_length=20)
    file_ext = models.CharField(max_length=6)
    createtime = models.DateField(auto_now=True)

    def __str__(self):
        return self.domain + '----' + self.file_ext

    class Meta:
        db_table = 'Dir_domain'
        ordering = ['id']


# class Dir_detail_manager(models.Manager):
#     def create(self, domain, dir, status):
#         dir_detail = self.model()
#         dir_detail.domain = domain
#         dir_detail.dir = dir
#         dir_detail.status = status
#         return dir_detail


class Dir_detail(models.Model):
    # 还没搞清楚ForeignKey的属性，再看看之后修改下面的代码
    # objects = Dir_detail_manager()
    domain = models.ForeignKey('Dir_domain', on_delete=models.CASCADE)
    dir = models.CharField(max_length=200)
    status = models.CharField(max_length=5)

    def __str__(self):
        return self.dir

    class Meta:
        db_table = 'Dir_detail'
        ordering = ['id']

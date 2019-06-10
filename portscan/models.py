from django.db import models

# Create your models here.

class Port_domain_manager(models.Manager):
    def isExists(self, domainName = ''):
        try:
            super(Port_domain_manager, self).get(domain=domainName)
        except:
            return False
        return True


class Port_domain(models.Model):
    objects = Port_domain_manager()
    domain = models.CharField(max_length=20)
    createtime = models.DateField(auto_now=True)

    class Meta:
        db_table = 'port_domain'
        ordering = ['id']

class Port_detail_manager(models.Manager):
    pass

class Port_detail(models.Model):
    objects = Port_detail_manager()
    domain = models.ForeignKey('Port_domain', on_delete=models.CASCADE)
    port = models.IntegerField()
    status = models.CharField(max_length=10)
    reason = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null=True)
    product = models.CharField(max_length=20, null=True)
    version = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'Port_detail'
        ordering = ['id']
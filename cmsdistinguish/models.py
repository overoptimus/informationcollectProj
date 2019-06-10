from django.db import models


# Create your models here.


class Cms_manager(models.Manager):
    def isExists(self, domain):
        try:
            super(Cms_manager, self).get(domain=domain)
        except:
            return False
        return True


class Cms(models.Model):
    objects = Cms_manager()
    domain = models.CharField(max_length=50)
    cmstype = models.CharField(max_length=20)
    createtime = models.DateField(auto_now=True)

    def __str__(self):
        return self.domain

    class Meta:
        db_table = 'Cms'
        ordering = ['id']

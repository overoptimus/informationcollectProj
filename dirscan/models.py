from django.db import models

# Create your models here.
class Url_manager(models.Manager):
    pass

class File_ext_manager(models.Manager):
    pass

class Url_status_manager(models.Manager):
    pass

class Url(models.Model):
    obj = Url_manager()
    url = models.CharField(max_length=20)

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'Url'
        ordering = ['id']

class File_ext(models.Model):
    obj = File_ext_manager()
    file_ext = models.CharField(max_length=20)

    def __str__(self):
        return self.file_ext

    class Meta:
        db_table = 'File_ext'
        ordering = ['id']

class Url_status(models.Model):
    obj = Url_status_manager()
    dir_path = models.CharField(max_length=20)
    status = models.IntegerField()
    url_id = models.ForeignKey('Url', on_delete=models.DO_NOTHING)
    file_ext_id = models.ForeignKey('File_ext', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.dir_path

    class Meta:
        db_table = 'Url_status'
        ordering = ['id']

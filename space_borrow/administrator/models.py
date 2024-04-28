from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class studentINFO(models.Model):
    request_id = models.IntegerField(blank=False, null=False, default=-1)  
    stu_id = models.CharField(max_length=255, primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'studentINFO'
        
class dormAdmin(AbstractUser):
    is_admin = models.BooleanField(verbose_name="Is admin", default=False)
    class Meta:
        managed = True
        db_table = 'dormAdmin'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Space(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    space_name = models.CharField(max_length=255)  # Field name made lowercase.
    region = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    eng_name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'Space'
        
class Register(models.Model):
    signature = models.CharField(max_length=255, primary_key=True, null=False, blank=False)
    start_time = models.IntegerField()  
    space = models.ForeignKey(Space, on_delete=models.CASCADE)  # Field name made lowercase. The composite primary key (Space_id, Start_time, Date) found, that is not supported. The first column is selected.
    date = models.DateField(null=False, blank=False)
    usable = models.IntegerField()
    user_id = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_phone = models.CharField(max_length=255, blank=True, null=True)
    user_dormnumber = models.IntegerField(blank=True, null=True)
    change_pwd = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Register'
        unique_together = ('space', 'start_time', 'date')



class BlackList(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=20)
    expire_time = models.DateField(blank=True, null=True)
    banned_reason = models.CharField(max_length=20, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'black_list'

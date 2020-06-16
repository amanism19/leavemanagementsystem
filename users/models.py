from django.db import models

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        managed= False
        db_table = 'roles'


class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed= False
        db_table = 'users_role'

class MenStu(models.Model):
    id = models.AutoField(primary_key = True)
    student_id = models.IntegerField()
    mentor_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ment_stu'

class Leave(models.Model):
    id = models.AutoField(primary_key = True)
    mentor_id = models.IntegerField()
    student_id = models.IntegerField()
    purpose = models.TextField()
    status = models.TextField()
    comment = models.TextField()
    duration = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    warden_start_date = models.DateTimeField() 
    warden_end_date = models.DateTimeField() 

    class Meta:
        managed = False
        db_table = 'Leave_Info'
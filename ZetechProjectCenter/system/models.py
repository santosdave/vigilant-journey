from django.db import models

class edAuditTrace(models.Model):
	action_id  = models.IntegerField(unique=True)
	act_user = models.CharField(max_length=10) 
	act_staffid = models.CharField(max_length=10) 
	act_descr  = models.CharField(max_length=100) 
	act_datetime = models.DateField() 
	act_other  = models.CharField(max_length=30) 

	def __str__(self):
		return self.act_user
from django.db import models

class Target (models.Model):
	url = models.CharField(max_length=300)

	def __unicode__(self):
		return self.url

class Link (models.Model):
	# id =  models.AutoField(primary_key=True)
	source = models.CharField(max_length=30, primary_key=True)
	target = models.ForeignKey(Target)

	def __unicode__(self):
		return self.source
# Create your models here.

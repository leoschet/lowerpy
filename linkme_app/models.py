from django.db import models

class Link (models.Model):
	id = models.AutoField(primary_key=True)
	source = models.ForeignKey(Source)
	target = models.CharField(max_length=30)

	def __unicode__(self):
		return self.id

class Source (models.Model):
	url = models.CharField(max_length=30)

	def __unicode__(self):
		return self.url
# Create your models here.

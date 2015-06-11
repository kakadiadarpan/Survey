from django.db import models


QUESTION_TYPES = (
	('mcq', 'Multiple Choice Question'),
	('sub', 'Subjective Question'),
)

# Create your models here.

class Questions(models.Model):
	question = models.CharField(max_length=1000)
	category = models.ManyToManyField('Category', blank=True, null=True)
	question_type = models.CharField(choices=QUESTION_TYPES, default='mcq', max_length=5)
	solution = models.TextField(blank=True, max_length=1000)
	number = models.IntegerField(default=0, null=True)
	def __unicode__(self):
		return self.question

class Category(models.Model):
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name
from django.core.exceptions import ValidationError
from django.contrib import admin
from questionbank.models import Questions, Category
import json

# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
	fieldsets = [
		('Question Details', {'fields': ['question', 'question_type', 'solution', 'number']}),
		(None,               {'fields': ['category']}),
	]
	list_display = ('question', 'question_type', 'solution', 'number')
	
	def save_model(self, request, obj, form, change):
		s_no = request.POST['number']
		count = Questions.objects.all().exclude(id=obj.id).filter(number=s_no).count()	
		if count<1:
			obj.save()
		else:
			raise ValidationError('Make sure that the value of number field is unique')

class CategoryAdmin(admin.ModelAdmin):
	fields = ['name']

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Category, CategoryAdmin)

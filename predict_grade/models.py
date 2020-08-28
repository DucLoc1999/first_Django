from djongo import models
from django import forms
from django.urls import reverse

class Inventory(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	price = models.IntegerField()

class Students(models.Model):
	# _id = models.IntegerField(primary_key=True)
	mssv = models.CharField(max_length=10)
	ho_ten = models.CharField(max_length=50)
	birth = models.DateField()

	def get_absolute_url(self):
		return reverse('students:detail', args=[self.id])

class StudentCreateForm(forms.ModelForm):
	fields = ['mssv', 'ho_ten', 'birth']
	mssv = forms.CharField(max_length=10)
	ho_ten = forms.CharField(max_length=50)
	birth = forms.DateTimeField()
	birth.input_formats = ['%d/%m/%Y']
	class Meta:
		model = Students
		fields = ('mssv', 'ho_ten', 'birth')

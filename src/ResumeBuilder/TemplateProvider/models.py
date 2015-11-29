from django.db import models

class Templates(models.Model):
	PDF = 'PDF'
	RESUME_FORMAT_CHOICES = (
		(PDF, 'PDF'),
	)
	template_name = models.CharField(max_length=200)
	template_body = models.TextField()
	resume_format = models.CharField(max_length=30,choices=RESUME_FORMAT_CHOICES, default=PDF)
	creation_date = models.DateTimeField('Date Published')

	def __str__(self):
		return self.template_name

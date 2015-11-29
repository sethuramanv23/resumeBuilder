from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	date_of_birth = models.DateTimeField('Date Of Birth')
	address = models.TextField()
	phone_number = models.CharField(max_length=15)
	email_id = models.EmailField()
	career_objective = models.TextField()

	def __str__(self):
		return self.first_name + " " + self.last_name

class Education(models.Model):
	HSC = 'HSC'
	UG = 'UG'
	PG = 'PG'
	PHD = 'PHD'
	OTHER = 'OTHER'
	DEGREE_LEVEL_CHOICES = (
		(HSC, 'HSC'),
		(UG, 'UG'),
		(PG, 'PG'),
		(PHD, 'PHD'),
		(OTHER, 'OTHER'),
	)
	user = models.ForeignKey(User)
	institute_name = models.CharField(max_length=300)
	degree = models.CharField(max_length=300)
	degree_level = models.CharField(max_length=30, choices=DEGREE_LEVEL_CHOICES, default=UG)
	percentage = models.FloatField()

	def __str__(self):
		return self.user.first_name
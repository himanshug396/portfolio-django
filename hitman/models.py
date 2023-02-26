from django.db import models
from ckeditor.fields import RichTextField

class AboutmeText(models.Model):
	name = models.CharField(max_length=1000)
	text = RichTextField(blank=True, null=True)
	use = models.BooleanField(default=False)

	def __str__(self):
		return str(self.name)

class NavigationItem(models.Model):
	name = models.CharField(max_length=1000)
	html_id = models.CharField(max_length=1000)
	url = models.CharField(max_length=1000, blank=True)
	show = models.BooleanField(default=True)
	rank = models.IntegerField()
	def __str__(self):
		return str(self.name)

class Quote(models.Model):
	text = models.CharField(max_length=1000)
	def __str__(self):
		return str(self.text)

class QuoteMe(models.Model):
	name = models.CharField(max_length=1000, blank=True)
	quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.name)

class ProjectCoverContainerType(models.Model):
	name = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='project_photo_containers')
	size = models.IntegerField()

	def __str__(self):
		return str(self.name)

class Project(models.Model):
	title = models.CharField(max_length=1000)
	position = models.CharField(max_length=1000, blank=True)
	company = models.CharField(max_length=1000, blank=True) 
	company_url = models.CharField(max_length=1000, blank=True)
	one_line_description = models.CharField(max_length=1000, blank=True)
	brief_description = models.CharField(max_length=1000, blank=True)
	full_description = RichTextField(blank=True, null=True)
	cover_image = models.ImageField(upload_to='project_photos')
	cover_image_type = models.ForeignKey(ProjectCoverContainerType, on_delete=models.CASCADE)
	full_image = models.ImageField(upload_to='project_photos')
	show = models.BooleanField(default=True)
	rank = models.IntegerField()

	def __str__(self):
		return str(self.rank) + ' : ' + str(self.title) + ' - ' + str(self.company)

class Skill(models.Model):
	name = models.CharField(max_length=1000)
	url = models.CharField(max_length=1000, blank=True)
	def __str__(self):
		return str(self.name)

class SocialMedia(models.Model):
	name = models.CharField(max_length=1000)
	fa_id = models.CharField(max_length=1000)
	url = models.CharField(max_length=1000)
	show = models.BooleanField(default=True)
	def __str__(self):
		return str(self.name)

class Resume(models.Model):
	name = models.FileField(upload_to='files')
	use = models.BooleanField(default=False)
	def __str__(self):
		return str(self.name)

class Query(models.Model):
	name = models.CharField(max_length=300)
	email = models.EmailField()
	phone = models.CharField(max_length=15, null=True)
	question = models.TextField()

	def __str__(self):
		return str(self.name) + "_" + str(self.question)
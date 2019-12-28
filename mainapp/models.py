from django.db import models

# Create your models here.
class contacte(models.Model):
	sender_name = models.CharField(max_length=50)
	send_title = models.CharField(max_length=50)
	send_date = models.DateTimeField(auto_now_add=True)
	sender_phone = models.CharField(max_length=15, blank=True)
	sender_email = models.EmailField()
	send_text = models.TextField(max_length=800)

	def __str__(self):
		return '{0}-{1}'.format(self.sender_name, self.send_title)

class carusel(models.Model):
	name = models.CharField(max_length=20)
	text = models.CharField(max_length=100)
	image = models.ImageField(upload_to="indexpic")

	def __str__(self):
		return self.name
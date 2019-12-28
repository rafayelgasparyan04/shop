from django.db import models

# Create your models here.

def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "productpic/% Y/% m/% d/{0}".format(filename)


class product(models.Model):
	name = models.CharField(max_length=50)
	add_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True, primary_key=True)
	best = models.BooleanField(default=False)
	available = models.BooleanField(default=True)
	category = models.ManyToManyField('categories', related_name='products')
	rate_count = models.IntegerField(default=0)
	rate_all = models.IntegerField(default=0)
	rate = models.FloatField(default=0)
	about = models.TextField(max_length=800)
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to="productpic/%Y/%m/%d")

	def __str__(self):
		return str(self.name)


class categories(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True, primary_key=True)

	def __str__(self):
		return str(self.name)
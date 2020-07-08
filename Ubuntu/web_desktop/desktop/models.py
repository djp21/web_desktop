from django.db import models
class desktop(models.Model):
	create_folder=models.CharField(max_length=30)
	create_file=models.CharField(max_length=30)
	trash=models.CharField(max_length=200)
	

from django.db import models
class Article(models.Model):
content = models.CharField(max_length=200)
#今回はcontentカラムを用意
def __str__(self):
	return self.content


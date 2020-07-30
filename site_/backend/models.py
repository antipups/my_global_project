from django.db import models

# Create your models here.


class News(models.Model):
    title_of_new = models.TextField()
    description_of_new = models.TextField()
    date_of_new = models.TextField()

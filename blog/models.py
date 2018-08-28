from django.db import models

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    link = models.URLField()
    image = models.ImageField(upload_to='blog',blank=True)

    def __str__(self):
        return self.title
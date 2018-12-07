from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='events',blank=True)

    def __str__(self):
        return self.title
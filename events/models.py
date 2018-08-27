from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    type = models.CharField(max_length=256, choices=[('local', 'local'), ('international','international')])
    image = models.ImageField(upload_to='events',blank=True)

    def __str__(self):
        return self.title
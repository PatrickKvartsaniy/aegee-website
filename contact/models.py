from django.db import models

# Create your models here.

class Board_member(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='board_photos',blank=True)

    def __str__(self):
        return self.title
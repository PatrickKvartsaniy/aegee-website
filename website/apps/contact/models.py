from django.db import models

# Create your models here.

class Board_member(models.Model):
    class Meta:
        verbose_name = "Board Member"
        verbose_name_plural = "Board Members"

    title = models.CharField(max_length=100)
    name_in_english = models.CharField(max_length=100)
    name_in_ukrainian = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='board_photos',blank=True)

    def __str__(self):
        return self.title
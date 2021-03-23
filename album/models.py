from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length= 60)
    pic = models.ImageField(upload_to = 'uploads')
    description = models.TextField()

    @classmethod
    def save_image(cls):
        image = cls.objects.all()
        return image


    def __str__(self):
        return self.name 
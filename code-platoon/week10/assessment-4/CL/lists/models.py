from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'Name:{self.name}'

class Post(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='posts')
    post_text = models.TextField()

    def __str__(self):
        return f'Catagory:{self.catagory} Post Text: {self.post_text}'

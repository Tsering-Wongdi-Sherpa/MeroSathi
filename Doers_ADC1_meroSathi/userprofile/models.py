from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    student_id = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to='profiles/',blank=True)
    def __str__(self):
        return self.user.username

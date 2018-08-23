from django.db import models
from users.models import CustomUser



class Job(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(blank=True)
    #created_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Job Title: {self.title} | Description: {self.description}'

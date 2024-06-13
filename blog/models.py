from django.db import models
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone

# class PostModel(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     pub_date = models.DateTimeField()
#     topic = models.CharField(max_length=100,default='default_value')  # Add topic field

#     def __str__(self):
#         return self.title
class PostModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    

    def __str__(self):
        return self.title


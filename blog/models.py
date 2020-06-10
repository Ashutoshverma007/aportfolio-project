from django.db import models

class Blog(models.Model):

    title= models.CharField(max_length=250)
    publish_date= models.DateTimeField()
    blog_body = models.TextField()
    image= models.ImageField(upload_to='image/')

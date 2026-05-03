from django.db import models

# model for themes

class sitesetting(models.Model):
    banner=models.ImageField(upload_to='media/site')
    caption=models.TextField()
    

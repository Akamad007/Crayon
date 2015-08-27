from django.db import models
from django.contrib.auth.models import User

class ApiFaviconUrl(models.Model):
    user = models.ForeignKey(User)
    base_url = models.URLField(unique = True )
    favicon = models.URLField()    
    createdDateTime = models.DateTimeField(auto_now_add = True)
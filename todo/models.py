import datetime
from django.conf import settings
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(
      default=datetime.date.today
      )
    user = models.ForeignKey(                   #ForeignKey verweißt auf ein anderes Model
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
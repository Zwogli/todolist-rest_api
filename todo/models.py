import datetime
from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(
      default=datetime.date.today
      )
    user = models.ForeignKey(                   #ForeignKey verweißt auf ein anderes Model
        User,
        on_delete=models.CASCADE,
        default=None,
    )
    
    def time_passed(self):
        current_date = date.today()
        time_passed = current_date - self.created_at
        return time_passed.days
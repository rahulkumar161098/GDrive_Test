
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Bid(models.Model):
   # id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   name=models.CharField(max_length=100)
   base_price= models.IntegerField()
   bid_date= models.DateField(auto_now_add=True)
   bid_desc= models.TextField()
   created_by=models.ForeignKey(to=User, on_delete=models.CASCADE)
   win_by= models.CharField(max_length=10, blank=True)
   bid_type= models.CharField(max_length=20, default="e_type")

   def __str__(self):
      return self.id
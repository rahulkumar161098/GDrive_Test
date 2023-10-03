from django.contrib import admin
from .models import CreateBid, CreatedUserBid

# Register your models here.
admin.site.register(CreateBid)
admin.site.register(CreatedUserBid)
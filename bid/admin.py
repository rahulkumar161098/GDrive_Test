from django.contrib import admin
from .models import CreateBid, CreatedUserBid

# Register your models here.

class CreatedBidView(admin.ModelAdmin):
   list_display=('name', 'base_price', 'created_by', 'win_by')
admin.site.register(CreateBid, CreatedBidView)

class BidsView(admin.ModelAdmin):
   list_display=('product_id', 'user_id', 'name', 'phone', 'email', 'bid_amount' )
admin.site.register(CreatedUserBid, BidsView)
from django.shortcuts import render
from .models import CreateBid

# Create your views here.

def getAllAuction(request):
   alldata= CreateBid.objects.all()
   # print(alldata)
   return render(request, 'home.html', {'bidData': alldata})

def auctionDetail(request, id):
   getAuctionDetails= CreateBid.objects.get(id=id)
   # print(getAuctionDetails)
   return render(request, 'AuctionDetails.html', {'data':getAuctionDetails})
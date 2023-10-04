from django.shortcuts import redirect, render
from .models import CreateBid, CreatedUserBid

# Create your views here.

def getAllAuction(request):
   try:
      alldata= CreateBid.objects.all()
      return render(request, 'home.html', {'bidData': alldata, 'count_down':24})
   except:
      return render(request, 'home.html')

def auctionDetail(request, id):
   try:
      getAuctionDetails= CreateBid.objects.get(id=id)      
      all_bids= CreatedUserBid.objects.filter(product_id=id)
      data={
         'product_details':getAuctionDetails,
         'all_bids':all_bids,
      }
      return render(request, 'AuctionDetails.html', {'data':data})
   except:
      return render(request, 'AuctionDetails.html')
   

def user_bid(request, id):
   if not request.user.is_authenticated:
      return redirect ('user_login')
   user_id = request.user.id
   if request.method== 'POST':
      bid_name= request.POST['bid_name']
      bid_email= request.POST['bid_email']
      phone= request.POST['phone']
      bid_amount= request.POST['bid_amount']
      bid_msg= request.POST['bid_msg']
      try:
         save_bid= CreatedUserBid.objects.create(product_id=id, user_id=user_id, name=bid_name, phone=phone, bid_amount=bid_amount, email=bid_email, bid_msg=bid_msg)
         save_bid.save()
         return render(request, 'home.html')
      except:
         return render(request, 'AuctionDetails.html')
   return render(request, 'bid_user_form.html')
   
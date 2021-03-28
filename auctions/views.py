from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError , models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from django import forms
from django.urls import reverse 
from .models import User,Bid,Listing,Comment,Category,Watchlist , Winner
from django.contrib import messages
from django.forms import ModelForm

def index(request):
 
 return render(
        request, "auctions/index.html", {"Listings":Listing.objects.filter(close = False)}
    )

def category(request , category_id):
    category = Listing.objects.filter(Category = category_id , close=False) #close to return only active listing
    return render(request ,"auctions/category.html" , {
        "categories":category
    } )
    


def create(request):

    if request.method == "POST": 
        title = request.POST["title"]
        price = request.POST["price"]
        explnation = request.POST["explnation"]
        url = request.POST["url"]
        holder = request.POST["holder"]
        cat = Category.objects.get(category=request.POST["category"])

        insta = Listing(
           title = title,
           price = price , 
           explnation = explnation , 
           link = url , 
           holder = holder , 
           bid = price,
           Category = cat

        )
        #if there is no photo uploaded
        if request.POST.get("url"):
            insta.link = request.POST.get("url")
        else:
            insta.link = "https://www.aust-biosearch.com.au/wp-content/themes/titan/images/noimage.gif"

       

        insta.save()

        return redirect(reverse("index"))
   
    return render(request, "auctions/create.html",{
      "categories":Category.objects.filter()
    })



def categories(request) :
    category = Category.objects.all()
    return render(request , "auctions/categories.html" ,{
    "categories":category
 })


def create_bid(request, listing_id):
    if request.method == "POST":
        Listing.objects.filter(pk = listing_id).update(bid=request.POST["bid"]) 
        listing = Listing.objects.get(id=listing_id)
        bid = Bid(user=request.user, listingid=listing , bid = request.POST["bid"])
        
        if listing.price < listing.bid:
         listing.bidder =str(bid.user)
         listing.save()
         bid.save()
    else:
            return viewlisting(request, listing_id)

    return HttpResponseRedirect(reverse("viewlisting", args=[listing_id]))


def watchlist(request):

    if request.method == "POST": 
            
        watchlist = Watchlist( 
            watchlist = request.POST["add-id"],
            user = request.user.id
        )

        watchlist.save() 

        return HttpResponseRedirect(reverse("watchlist"))

    return render(request, "auctions/watchlist.html", {
        "watchlist": Watchlist.objects.filter(user=request.user.id),
        "listings": Listing.objects.filter(close=False)
    })
def remove(request):

    remove = Watchlist.objects.filter(user=request.user.id, watchlist=request.POST["remove-it"]) 
    remove.delete()

    return HttpResponseRedirect(reverse("watchlist"))    
   
def viewlisting(request , listing_id):
    watchlist = Watchlist.objects.filter(watchlist = listing_id)
    comments = Comment.objects.filter(list_id= listing_id)
    lists = Listing.objects.get(id = listing_id , close = False)
    mini = lists.bid + 1 
    
    if request.method == "POST":
      Listing.objects.filter(id = listing_id).update(bid = request.POST["bid"])
      Listing.objects.filter(id = listing_id).update(bidder= request.user.username)
      lists.save()

      return HttpResponseRedirect(reverse("viewlisting" , args=[listing_id]))
    else:
        return render(request , "auctions/viewlisting.html", {
            "listings":lists , 
            "comments":comments, 
            "watchlist":watchlist,
            "minimum":mini 
        })

def addcomment(request , listing_id):
   
   if request.method=="POST" :

       comment = Comment(
           comment = request.POST["comment"],
           user = request.user , 
           list_id = listing_id
       )
       comment.save()

       return HttpResponseRedirect(reverse("viewlisting" , args=[listing_id]))

def close(request):
    if request.method == "POST":
        Listing.objects.filter(id = request.POST["listing_id"]).update(close = True)

        return HttpResponseRedirect(reverse("close"))

    return render(request , "auctions/closed.html" , {
            "list":Listing.objects.filter(close=True)
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        phone = request.POST["phone"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username = username, email = email, password = password , phone = phone , first_name = first_name , last_name = last_name , address = address)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



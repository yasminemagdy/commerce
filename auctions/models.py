from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass
    address = models.CharField(max_length=200 , default="")
    phone = models.IntegerField(default=0)

class Category(models.Model):
    category = models.CharField(max_length=64 , null=True , blank=True)
    close = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category}"


class Listing(models.Model):
    holder = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    explnation = models.TextField()
    price = models.IntegerField()
    bid = models.IntegerField(null=True)
    link = models.URLField()
    time = models.DateTimeField(default=timezone.now)
    bidder = models.CharField(max_length=64 , null=True , default="No one!")
    close = models.BooleanField(default=False)
    Category = models.ForeignKey(Category , on_delete = models.CASCADE , related_name="model" , null=True , blank=True)
    watchers = models.ManyToManyField(User, blank=True, related_name="watched_listings")
 

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids' , default=0)
    listingid =  models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids' , default="")
    bid = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    close = models.BooleanField(default=False)

class Comment(models.Model):
    holder = models.CharField(max_length=64)
    time = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    list_id = models.IntegerField()
    user = models.CharField(max_length=32 , default=64)

    
    
class Watchlist(models.Model):
    watchlist = models.IntegerField()
    user = models.IntegerField()
    listing_id = models.IntegerField(default=32)

class Winner(models.Model):
    owner = models.CharField(max_length=64)
    winner_id = models.IntegerField( default= int)
    listingid = models.IntegerField()
    winprice = models.IntegerField()
    title = models.CharField(max_length=64, null=True)
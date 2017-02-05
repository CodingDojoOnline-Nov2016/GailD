from __future__ import unicode_literals
from ..myLoginReg.models import User
from django.db import models

# Create your models here.
class User_Wishlist(models.Model):
    item = models.ForeignKey('others_wishlist')
    added_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Others_Wishlist(models.Model):
    item = models.ForeignKey('user_wishlist')
    added_by = models.CharField(max_length=50)
    #author = models.ForeignKey('Author') #a person can be an author of many books
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ListManager(models.Manager):
    def create_list(self, form_data, user_id):

        try:
            list = self.fetch_userlist(form_data)
            print list
            # We have the book, now let's grab the user object
            user = User.objects.get(id=user_id)
            new_list = NewList.objects.create(content=form_data['new_item'])
            return (True, new_list)
        except:
            return (False, ["There was a problem creating the new wish list item..."])

    def fetch_userlist(self, form_data):

        try:
            u_wishlist = User_Wishlist.objects.get(id=form_data['user_wishlist_id'])
        except:
            u_wishlist = User_Wishlist.objects.create(title=form_data['new_item'])
        return book

    def fetch_otherlist(self, form_data):
        try:
            o_wishlist = Others_Wishlist.objects.get(id=form_data['others_wishlist_id'])
        except:

            o_wishlist = Others_Wishlist.objects.create(name=form_data['item'])
        return o_wishlist

    def fetch_recent(self):
        return NewList.objects.all().order_by('-created_at')[:3]

class NewList(models.Model):
    item = models.TextField()
    #user = models.ForeignKey('myLoginReg.User') #points to my LoginReg database, a user can have many book reviews
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ListManager()

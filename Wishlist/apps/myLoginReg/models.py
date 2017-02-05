from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Count
import bcrypt

#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class UserManager(models.Manager):
    def validate_register(self, request):
        errors = self.validate_form(request)
        if len(errors) > 0:
            return (False, errors)
        # No errors, time to hash the pw
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        # pw is hashed, time to create new user
        user = self.create(name=request.POST['name'], username=request.POST['username'], pw_hash=pw_hash)
        return (True, user)

    def validate_login(self, request):
        try:
            user = User.objects.get(username=request.POST['username'])
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode()):
                return (True, user)
        except ObjectDoesNotExist:
            pass
        return (False, ["Username or password does not match."])


    def validate_form(self, request):
        errors = []
        if len(request.POST['name']) < 3 or len(request.POST['username']) < 3 or len(request.POST['date']) < 1:
            errors.append('Name field and/or username field cannot be empty or must be greater than three characters')
        if len(request.POST['password']) > 8 or len(request.POST['password']) != len(request.POST['pw_chk']):
            errors.append('Passwords must match and be at least 8 characters')
        return errors

    def fetch_user_info(self, id):
        return self.filter(id=id).annotate(total_reviews=Count('review'))[0]

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

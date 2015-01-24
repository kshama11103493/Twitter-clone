from django.db import models
from django.contrib.auth.models import User
"""django.contrib.auth:-contains the core of the authentication framework, and its default models.
It handles user accounts, groups, permissions and cookie-based user sessions
"""
import hashlib
"""The hashlib module, included in The Python Standard library is a module
containing an interface to the most popular hashing algorithms """


class K_twitter(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)

"""django.db.models:-A model is the single, definitive source of information about your data.
For Example Here: content (max character 100 ),user , creation_data create table
automatically in database.
"""

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

"""similarly it also create table automatically in database."""   
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


# Create your models here.

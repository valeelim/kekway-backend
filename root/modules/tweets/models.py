from django.db import models

# Create your models here.
from root.modules.accounts.models import UserAccount

class Tweet(models.Model):
    desc = models.TextField(blank=False, null=False)
    close_only = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)


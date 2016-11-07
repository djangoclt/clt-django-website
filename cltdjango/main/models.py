from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group


class ActiveMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateJoined = models.DateTimeField()
    githubUrl = models.URLField()
    linkedInUrl = models.URLField()
    photo = models.URLField()

    def __str__(self):
        return self.user.username

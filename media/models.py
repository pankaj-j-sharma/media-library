from pyexpat import model
from tkinter import CASCADE, CURRENT
from unicodedata import category
from django.db import models
from sqlalchemy import true
from datetime import datetime

from user_auth.models import User


def user_directory_path(self, filename):
    # print('dir', dir(self))
    return 'uploads/user_{0}/{1}'.format(getattr(self, "Created By_id"), filename)


class MediaCategory(models.Model):
    class Meta:
        verbose_name = "Media Category"
        verbose_name_plural = "Media Categories"
        db_table = 'Media_Category'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    created = models.DateTimeField('Created On', default=datetime.now)
    updated = models.DateTimeField('Updated On', default=datetime.now)
    is_active = models.BooleanField(default=true)


class MediaType(models.Model):
    class Meta:
        verbose_name = "Media Type"
        verbose_name_plural = "Media Types"
        db_table = 'Media_Type'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    created = models.DateTimeField('Created On', default=datetime.now)
    updated = models.DateTimeField('Updated On', default=datetime.now)
    is_active = models.BooleanField(default=true)


class MediaItem(models.Model):
    class Meta:
        verbose_name = "Media Item"
        verbose_name_plural = "Media Items"
        db_table = 'Media_Item'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    type = models.ForeignKey(MediaType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        MediaCategory, on_delete=models.SET_NULL, null=True)
    path = models.FileField(upload_to=user_directory_path)
    size = models.BigIntegerField(default=0)
    created_on = models.DateTimeField('Created On', default=datetime.now)
    updated_on = models.DateTimeField('Updated On', default=datetime.now)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, name='Created By', related_name='+')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL,  null=True, name='Updated By', related_name='+')

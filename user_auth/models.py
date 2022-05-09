from django.db import models


class User(models.Model):
    class Meta:
        verbose_name = "Media User"
        verbose_name_plural = "Media Users"
        db_table = 'Media_User'

    def __str__(self):
        return self.name

    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=200)
    last_login = models.DateTimeField('Last Login')

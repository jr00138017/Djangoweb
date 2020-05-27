from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=15, null=True)
    user_passwd = models.CharField(max_length=20, null=True)
    user_ticket = models.CharField(max_length=30, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    last_modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'login_info'

from django.db import models

class User(models.Model):
    # ユーザID
    user_id = models.IntegerField()
    # ユーザ名
    user_name = models.CharField(max_length=128)
    # 登録日
    registered_at = models.DateTimeField()

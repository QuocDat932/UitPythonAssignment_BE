from django.db import models


class Role(models.Model):

    class Meta:
        # Định nghĩa tên bảng trong CSDL
        db_table = 'UIT_ROLE'

    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_use = models.IntegerField()


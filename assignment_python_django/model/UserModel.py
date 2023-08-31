from django.db import models
from assignment_python_django.model.Role import Role


class User(models.Model):
    class Meta:
        db_table = "UIT_USER"

    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    mssv = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    img = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    birthday = models.DateTimeField
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_column='USER_ROLE')
    is_use = models.IntegerField()


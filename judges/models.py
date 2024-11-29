from django.db import models

# Create your models here.

# Create your models here.
class Judge(models.Model):
    judge_name = models.CharField(max_length = 50)
    user_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 30)
    img = models.ImageField(upload_to = 'judge/')
    status = models.CharField(max_length = 100, default = 'active')

    class Meta:
        db_table = "judge"
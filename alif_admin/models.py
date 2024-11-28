from django.db import models
from judges.models import Judge
# Create your models here.

class AlifAdmin(models.Model):
    admin_id = models.IntegerField()
    password = models.CharField(max_length = 30)

    class Meta:
        db_table = "alif_admin"


class Participant(models.Model):
    student_name = models.CharField(max_length = 50)
    admission_no = models.CharField(max_length = 20)
    student_cls = models.CharField(max_length = 20)
    division = models.CharField(max_length = 30)
    category = models.CharField(max_length = 30, default = "Category-1")
    status = models.CharField(max_length = 100, default = 'active')
    added_date = models.DateTimeField(auto_now_add=True)
    code_letter = models.CharField(max_length = 20, default ="" )
    
    
    class Meta:
        db_table = "participant"

class Score(models.Model):
    student = models.ForeignKey(Participant, on_delete = models.CASCADE)
    rubrics1 = models.FloatField()
    rubrics2 = models.FloatField()
    rubrics3 = models.FloatField()
    rubrics4 = models.FloatField()
    rubrics5 = models.FloatField()
    rubrics6 = models.FloatField()
    rubrics7 = models.FloatField()
    comments = models.CharField(max_length=200)
    judge = models.ForeignKey(Judge, on_delete = models.SET_NULL, null = True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        db_table = "score"
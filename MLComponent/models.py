from django.db import models

# Create your models here.
class ContentBasedFinalDf(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.TextField(blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    course_level = models.IntegerField(blank=True, null=True)
    course_provider = models.TextField(blank=True, null=True)
    register_agent = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_based_final_df'


class PredictionsQuizDf(models.Model): 
    uid = models.BigIntegerField()
    iid = models.BigIntegerField()
    r_ui = models.FloatField()
    est = models.FloatField()
    details = models.JSONField()

    class Meta: 
        managed = False
        db_table = 'predictions_quiz_df'



class PredictionsAssnDf(models.Model): 
    uid = models.BigIntegerField()
    iid = models.BigIntegerField()
    r_ui = models.FloatField()
    est = models.FloatField()
    details = models.JSONField()

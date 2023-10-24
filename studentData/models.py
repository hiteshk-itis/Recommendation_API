# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class StdAssignment(models.Model):
    student_id = models.IntegerField(primary_key=True)
    assignment_id = models.IntegerField(blank=True, null=True)
    full_marks = models.IntegerField(blank=True, null=True)
    obtained_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'std_assignment'


class StdLog(models.Model):
    student_id = models.IntegerField(primary_key=True)
    login_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'std_log'


class StdQuiz(models.Model):
    student_id = models.IntegerField(primary_key=True)
    quiz_id = models.IntegerField(blank=True, null=True)
    full_marks = models.IntegerField(blank=True, null=True)
    obtained_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'std_quiz'

class RefinedRating(models.Model): 
    student = models.IntegerField(blank=True, null=True)
    course_code = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta: 
        managed = False
        db_table = 'refined_rating_table'
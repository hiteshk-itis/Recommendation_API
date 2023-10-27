from django.db import models

# Create your models here.
class UserListRaw(models.Model): 
    id = models.IntegerField(primary_key=True)
    username = models.TextField(blank = True, null = True)
    first_name = models.TextField(blank = True, null = True)
    last_name = models.TextField(blank = True, null = True)
    email = models.TextField(blank = True, null = True)
    is_active = models.TextField(blank = True, null = True)
    member_id = models.TextField(blank = True, null = True)
    member_permanent_address = models.TextField(blank = True, null = True)
    member_temporary_address = models.TextField(blank = True, null = True)
    member_birthdate = models.TextField(blank = True, null = True)
    member_phone = models.TextField(blank = True, null = True)
    use_flag = models.IntegerField(blank = True, null = True)
    register_agent = models.TextField(blank = True, null = True)
    register_datetime = models.TextField(blank = True, null = True)
    updated_datetime = models.TextField(blank = True, null = True)
    is_teacher = models.IntegerField(blank = True, null = True)
    is_student = models.IntegerField(blank = True, null = True)  
    is_center_admin = models.IntegerField(blank = True, null = True)
    member_memo = models.TextField(blank = True, null = True)
    member_avatar = models.TextField(blank = True, null = True)
    member_department = models.TextField(blank = True, null = True)
    member_position = models.TextField(blank = True, null = True)
    center_code = models.IntegerField(blank=True, null=True)
    # password = models.TextField(blank = True, null = True)
    # member_gender = models.TextField(blank = True, null = True)

class CourseInfoRaw(models.Model):
    id = models.IntegerField(primary_key=True)
    course_name = models.TextField(blank=True, null=True)
    course_code = models.TextField(blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    course_cover_file = models.TextField(blank=True, null=True)
    course_level = models.IntegerField(blank=True, null=True)
    course_info = models.TextField(blank=True, null=True)
    use_flag = models.TextField(blank=True, null=True)
    register_datetime = models.TextField(blank=True, null=True)
    updated_datetime = models.TextField(blank=True, null=True)
    register_agent = models.TextField(blank=True, null=True)
    course_provider = models.TextField(blank=True, null=True)
    syllabus = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    center_code = models.IntegerField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)



class CourseRatingRaw(models.Model):
    rating_id = models.IntegerField(primary_key = True)
    rating = models.FloatField(blank=True, null=True)
    chapter_code = models.IntegerField(blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    course_code = models.IntegerField(blank=True, null=True)
    center_code = models.IntegerField(blank=True, null=True)

class TagsRaw(models.Model): 
    id = models.IntegerField(primary_key=True)
    tag_name = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null = True)


class RawTablesInfo(models.Model):
    id = models.AutoField(primary_key=True) 
    tableName = models.TextField(blank=False, null=False)
    numData = models.IntegerField(blank=False, null=False)
    lastPage = models.IntegerField(blank = False, null = False)
    dateTime = models.DateTimeField(auto_now_add=True)

# Create your models here.
class UserListPreprocessed(models.Model): 
    id = models.IntegerField(primary_key=True)
    username = models.TextField(blank = True, null = True)
    first_name = models.TextField(blank = True, null = True)
    last_name = models.TextField(blank = True, null = True)
    email = models.TextField(blank = True, null = True)
    is_active = models.BooleanField(blank = True, null = True)
    member_id = models.TextField(blank = True, null = True)
    member_permanent_address = models.TextField(blank = True, null = True)
    member_temporary_address = models.TextField(blank = True, null = True)
    member_birthdate = models.DateTimeField(blank = True, null = True)
    member_phone = models.TextField(blank = True, null = True)
    use_flag = models.BooleanField(blank = True, null = True)
    register_agent = models.TextField(blank = True, null = True)
    register_datetime = models.DateTimeField(blank = True, null = True)
    updated_datetime = models.DateTimeField(blank = True, null = True)
    is_teacher = models.BooleanField(blank = True, null = True)
    is_student = models.BooleanField(blank = True, null = True)  
    is_center_admin = models.BooleanField(blank = True, null = True)
    member_memo = models.TextField(blank = True, null = True)
    member_avatar = models.TextField(blank = True, null = True)
    member_department = models.FloatField(blank = True, null = True)
    member_position = models.TextField(blank = True, null = True)
    center_code = models.IntegerField(blank=True, null=True)
    # password = models.TextField(blank = True, null = True)
    # member_gender = models.TextField(blank = True, null = True)

class CourseInfoPreprocessed(models.Model):
    id = models.IntegerField(primary_key=True)
    course_name = models.TextField(blank=True, null=True)
    center_code = models.IntegerField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    



class CourseRatingPreprocessed(models.Model):
    # id = models.IntegerField(primary_key=True)
    student = models.IntegerField(blank=True, null=True)
    course_code = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

class TagsPreprocessed(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.TextField(null=True, blank=True)
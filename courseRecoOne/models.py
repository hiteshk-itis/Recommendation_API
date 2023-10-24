# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Hero(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'courseRecoOne_hero'

class UserList(models.Model): 
    id = models.IntegerField(primary_key=True)
    username = models.TextField(blank = True, null = True)
    first_name = models.TextField(blank = True, null = True)
    last_name = models.TextField(blank = True, null = True)
    email = models.TextField(blank = True, null = True)
    member_id = models.TextField(blank = True, null = True)
    password = models.TextField(blank = True, null = True)
    member_permanent_address = models.TextField(blank = True, null = True)
    member_temporary_address = models.TextField(blank = True, null = True)
    member_birthdate = models.TextField(blank = True, null = True)
    member_phone = models.TextField(blank = True, null = True)
    use_flag = models.IntegerField(blank = True, null = True)
    
    register_datetime = models.TextField(blank = True, null = True)
    updated_datetime = models.TextField(blank = True, null = True)
    member_memo = models.TextField(blank = True, null = True)
    member_avatar = models.TextField(blank = True, null = True)
    is_teacher = models.IntegerField(blank = True, null = True)
    is_student = models.IntegerField(blank = True, null = True)  
    member_gender = models.TextField(blank = True, null = True)
    center_code = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'user_list'


class CourseAnalytics(models.Model):
    id = models.IntegerField(primary_key=True)
    course = models.IntegerField(blank=True, null=True)
    forum_count = models.IntegerField(blank=True, null=True)
    quiz_count = models.IntegerField(blank=True, null=True)
    assignment_count = models.IntegerField(blank=True, null=True)
    video_count = models.IntegerField(blank=True, null=True)
    pdf_count = models.IntegerField(blank=True, null=True)
    ppt_count = models.IntegerField(blank=True, null=True)
    images_count = models.IntegerField(blank=True, null=True)
    text_count = models.IntegerField(blank=True, null=True)
    chapters_count = models.IntegerField(blank=True, null=True)
    running_time = models.IntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_analytics'


class CourseInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    course_name = models.TextField(blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    course_cover_file = models.TextField(blank=True, null=True)
    course_level = models.IntegerField(blank=True, null=True)
    course_info = models.FloatField(blank=True, null=True)
    use_flag = models.IntegerField(blank=True, null=True)
    register_datetime = models.TextField(blank=True, null=True)
    updated_datetime = models.TextField(blank=True, null=True)
    register_agent = models.TextField(blank=True, null=True)
    course_provider = models.TextField(blank=True, null=True)
    syllabus = models.TextField(blank=True, null=True)
    keyword = models.FloatField(blank=True, null=True)
    center_code = models.FloatField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    recommended_course = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_info'


class CourseList(models.Model): 

    id = models.IntegerField(primary_key=True)
    course_name = models.TextField(blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    course_cover_file = models.TextField(blank=True, null=True)
    course_level = models.IntegerField(blank=True, null=True)
    course_info = models.TextField(blank=True, null=True)
    use_flag = models.IntegerField(blank=True, null=True)
    register_datetime = models.TextField(blank=True, null=True)
    updated_datetime = models.TextField(blank=True, null=True)
    register_agent = models.TextField(blank=True, null=True)
    course_provider = models.TextField(blank=True, null=True)
    syllabus = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    center_code = models.FloatField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    recommended_course = models.TextField(blank=True, null=True)

    class Meta: 
        managed = False
        db_table = 'course_list'

class CourseRating(models.Model):
    rating_id = models.IntegerField(primary_key = True)
    rating = models.FloatField(blank=True, null=True)
    chapter_code = models.IntegerField(blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    course_code = models.IntegerField(blank=True, null=True)
    center_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_rating'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Keywords(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'


class ServerCourse(models.Model):
    id = models.IntegerField(primary_key=True)
    course_name = models.TextField(blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    course_level = models.IntegerField(blank=True, null=True)
    course_info = models.FloatField(blank=True, null=True)
    updated_datetime = models.TextField(blank=True, null=True)
    course_provider = models.TextField(blank=True, null=True)
    center_code = models.IntegerField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_course'


class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'

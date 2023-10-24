from rest_framework import serializers
from .models import Hero, CourseAnalytics, CourseInfo, CourseRating, Keywords, Tags, ServerCourse, CourseList, UserList
class HeroSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Hero
        fields = ('id', 'name', 'alias')
        
class UserListSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = UserList
        fields = '__all__'


class CourseAnalyticsSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = CourseAnalytics
        fields = '__all__'
        

class CourseInfoSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = CourseInfo
        fields = '__all__'

class CourseListSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = CourseList
        fields = '__all__'

class CourseNameSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = CourseInfo
        fields=['url','id','course_name']

class CourseRatingSerializer(serializers.HyperlinkedModelSerializer): 
    rating_id = serializers.ReadOnlyField()
    class Meta: 
        model = CourseRating
        fields = '__all__'

class KeywordsSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = Keywords
        fields = '__all__'

class TagsSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = Tags
        fields = '__all__'

class ServerCourseSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField()
    class Meta: 
        model = ServerCourse
        fields = '__all__'
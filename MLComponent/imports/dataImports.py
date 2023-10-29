import numpy as np 
import pandas as pd

data_course_list = pd.DataFrame.from_records(CourseInfoPreprocessed.objects.all().values())

data_user_list = pd.DataFrame.from_records(UserListPreprocessed.objects.all().values())

data_rating = pd.DataFrame.from_records(CourseRatingPreprocessed.objects.all().values())
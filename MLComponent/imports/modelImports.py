import numpy as np
import pandas as pd
from ..models import PredictionsRatingDf
import pickle
# content_based
# cosine_sim = np.load('models/content_based/cosineSim.pkl', allow_pickle=True)
# file = open("models/content_based/cosineSim.pkl",'rb')
# cosine_sim = pickle.load(file)
# file.close()
predictions_df = pd.DataFrame.from_records(PredictionsRatingDf.objects.all().values())

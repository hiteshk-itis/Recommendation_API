import numpy as np
import pandas as pd
from ..models import PredictionsRatingDf

# content_based
cosine_sim = np.load('models/content_based/cosineSim.pkl', allow_pickle=True)

predictions_df = pd.DataFrame.from_records(PredictionsRatingDf.objects.all().values())

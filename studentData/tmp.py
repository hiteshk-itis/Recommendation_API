import pandas as pd
from models import RefinedRating

ratings = pd.read_pickle("rating.pkl")

df = ratings
model_df = RefinedRating

predictions_records = df.to_dict('records')
model_df.objects.all().delete()
model_instances = [
    model_df(
        uid = predictions_record['uid'], 
        iid = predictions_record['iid'], 
        r_ui = predictions_record['r_ui'], 
        est = predictions_record['est'], 
        details = predictions_record['details'], 
    )
    for predictions_record in predictions_records
]
model_df.objects.bulk_create(model_instances)


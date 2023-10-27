import numpy as np
import pandas as pd

def mapIdsToAnotherDf(idList: list, referenceDf: pd.DataFrame):
    res = []
    if not pd.isna([idList]).any():
        for i in idList:
            res.extend(referenceDf[referenceDf['id']==i]["tag_name"])
        return res
    else:
        return ''

def applyLowerCase(val: str) -> str:
    if isinstance(val, str):
        return str.lower(val)
    else:
        return ''
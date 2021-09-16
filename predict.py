import os
import requests


def predict_authors_gender(text: str, model: str):
    print(text, model)
    url = os.getenv("prediction_api_url") + '/bertSeqCls'
    res = requests.post(url, json={'content': text})
    print(res.url)

    if model == 'albert_FT' or 'xgboost':
        return res.json()['predict']

    else:
        return res.json()

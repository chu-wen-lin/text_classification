import requests
import pandas as pd
from typing import List, Dict


def access_to_posts(api_url: str, query_params: Dict[str, any]) -> object:
    """
    :param api_url: The url of mysql_api which is saved in the environment variable.
    :param query_params: Must be declared to be dictionary type. Notice: format of value of keywords is List[str].
    :return: A List of json.
    """

    try:
        response = requests.get(url=api_url, params=query_params)  # send a GET request to api
        if response.status_code == requests.codes.ok:
            print("OK!")
        print(response.url)
        posts: List[Dict[str, any]] = response.json()  # format response data as JSON
        return posts

    except requests.RequestException as error:
        print(error)


def convert_json_to_dataframe(posts: List[str]):
    df = pd.json_normalize(posts)
    return df

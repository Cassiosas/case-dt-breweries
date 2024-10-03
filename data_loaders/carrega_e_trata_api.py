import io
import pandas as pd
import requests
import json
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://api.openbrewerydb.org/breweries'
    response = requests.get(url)
    chamada = response.json()

    data = json.dumps(chamada)

    j = json.loads(json.dumps(data))

    df = j.replace('null', '"N/A"')

    df_final = pd.DataFrame(eval(df))

    return df_final


@test
def test_output(output, *args) -> None:
    print(len(output))
    assert output is not None, 'The output is undefined'

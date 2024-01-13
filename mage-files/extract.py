import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Fazer o Load dos dados da por API aqui 
    segue um exemplo de url
    """
    url = 'https://storage.googleapis.com/uber-data-engineering-project-FAL/uber_data.csv'
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Pode ser usado para testar a saído dos dados
    """
    assert output is not None, 'The output is undefined'

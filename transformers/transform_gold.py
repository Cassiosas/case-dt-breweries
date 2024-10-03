from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:

    result = df.groupby(['state_province', 'brewery_type']).size().reset_index(name='count')

    result_sort = result.sort_values(by='count', ascending=False)

    return result_sort


@test
def test_output(output, *args) -> None:

    print(output)

    assert output is not None, 'The output is undefined'

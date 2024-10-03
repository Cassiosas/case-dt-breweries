from deltalake.writer import write_deltalake
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(df, *args, **kwargs):
    storage_options = {
        'AZURE_STORAGE_ACCOUNT_NAME': 'datalakebreweries',
        'AZURE_STORAGE_ACCOUNT_KEY': 'MQAB8GccKbGAwKOQ7YxEy+nrRYC8/M4h+uUMLYKI0ePxNgSNReNWDre1c9ilzY3wwJi5xSmWhsTL+AStAexyig==',
        'AZURE_STORAGE_CLIENT_ID': 'd639bb9a-adf4-4f80-b950-ca9c4eed439d',
        'AZURE_STORAGE_CLIENT_SECRET': '00f88568-d7d0-4003-9cef-a89092f1cc59',
        'AZURE_STORAGE_TENANT_ID': '4089272c-0e47-4d4f-81f7-58eec2bdb4f1',
    }

    uri = 'abfss://breweries@datalakebreweries.dfs.core.windows.net/Gold/'

    write_deltalake(
        uri,
        data=df,
        mode='overwrite',       
        overwrite_schema=False, 
        storage_options=storage_options,
    )

from deltalake.writer import write_deltalake
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(df, *args, **kwargs):
    storage_options = {
        'AZURE_STORAGE_ACCOUNT_NAME': '<removidos_por_seguranca-estao_no_original>',
        'AZURE_STORAGE_ACCOUNT_KEY': 'removidos_por_seguranca-estao_no_original',
        'AZURE_STORAGE_CLIENT_ID': 'removidos_por_seguranca-estao_no_original',
        'AZURE_STORAGE_CLIENT_SECRET': 'removidos_por_seguranca-estao_no_original',
        'AZURE_STORAGE_TENANT_ID': 'removidos_por_seguranca-estao_no_original',
    }

    uri = 'abfss://removidos_por_seguranca-estao_no_original/Gold/'

    write_deltalake(
        uri,
        data=df,
        mode='overwrite',       
        overwrite_schema=False, 
        storage_options=storage_options,
    )

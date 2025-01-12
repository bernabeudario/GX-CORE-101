import great_expectations as gx

context = gx.get_context(mode="file")

datasource_name = "DS Taxi"
data_source = context.data_sources.get(datasource_name)

asset_name = "nyc_taxi_data"
data_asset = data_source.get_asset(asset_name)

full_table_batch_definition = data_asset.add_batch_definition_whole_table(
    name="FULL_TABLE"
)
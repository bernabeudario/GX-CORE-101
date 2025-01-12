import great_expectations as gx

context = gx.get_context(mode="file")

data_source_name = "DS Taxi"
data_source = context.data_sources.get(data_source_name)

asset_name = "nyc_taxi_data"
database_table_name = "nyc_taxi_data"
table_data_asset = data_source.add_table_asset(
    table_name=database_table_name, name=asset_name
)

print(data_source.assets)